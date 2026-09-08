param([Parameter(Mandatory = $true)][string]$ConfigPath)

Add-Type -AssemblyName System.Drawing

$Dpi = 300
$BleedIn = 0.125
$PaperThickness = @{ bw_white = 0.002252; bw_cream = 0.0025; color = 0.002347 }

function Convert-InchesToPixels([double]$Inches) {
    return [int][Math]::Round($Inches * $Dpi)
}

function Convert-HexColor([string]$Hex) {
    $clean = $Hex.TrimStart('#')
    return [System.Drawing.Color]::FromArgb(
        [Convert]::ToInt32($clean.Substring(0, 2), 16),
        [Convert]::ToInt32($clean.Substring(2, 2), 16),
        [Convert]::ToInt32($clean.Substring(4, 2), 16))
}

function New-CoverFont([int]$PixelSize, [bool]$Bold = $true) {
    $style = if ($Bold) { [System.Drawing.FontStyle]::Bold } else { [System.Drawing.FontStyle]::Regular }
    return New-Object System.Drawing.Font('Times New Roman', $PixelSize, $style, [System.Drawing.GraphicsUnit]::Pixel)
}

function Measure-TextWidth($Graphics, [string]$Text, $Font) {
    return $Graphics.MeasureString($Text, $Font, [int]::MaxValue, [System.Drawing.StringFormat]::GenericTypographic).Width
}

function Get-WrappedLines($Graphics, [string]$Text, $Font, [double]$MaxWidth) {
    $lines = New-Object System.Collections.Generic.List[string]
    $line = ''
    foreach ($word in ($Text -split '\s+')) {
        if (-not $word) { continue }
        $trial = (($line + ' ' + $word).Trim())
        if ((Measure-TextWidth $Graphics $trial $Font) -le $MaxWidth) {
            $line = $trial
        }
        else {
            if ($line) { $lines.Add($line) }
            $line = $word
        }
    }
    if ($line) { $lines.Add($line) }
    return ,$lines.ToArray()
}

function Get-FittedTitle($Graphics, [string]$Text, [double]$SafeWidth, [double]$TrimWidth) {
    $scale = $TrimWidth / 8.5
    for ($pt = 90; $pt -ge 36; $pt -= 2) {
        $pixelSize = [Math]::Max(12, [int][Math]::Round($pt * $scale * $Dpi / 72.0))
        $font = New-CoverFont $pixelSize $true
        $lines = Get-WrappedLines $Graphics $Text $font $SafeWidth
        $allFit = $true
        foreach ($line in $lines) {
            if ((Measure-TextWidth $Graphics $line $font) -gt $SafeWidth) { $allFit = $false; break }
        }
        if (($lines.Count -gt 0) -and ($lines.Count -le 4) -and $allFit) {
            return [pscustomobject]@{ Font = $font; Lines = $lines; PointSize = $pt }
        }
        $font.Dispose()
    }
    $pixelSize = [Math]::Max(12, [int][Math]::Round(36 * $scale * $Dpi / 72.0))
    $font = New-CoverFont $pixelSize $true
    return [pscustomobject]@{ Font = $font; Lines = (Get-WrappedLines $Graphics $Text $font $SafeWidth); PointSize = 36 }
}

function Draw-CoverFit($Graphics, $Image, [System.Drawing.Rectangle]$Target) {
    $ratio = [Math]::Max($Target.Width / $Image.Width, $Target.Height / $Image.Height)
    $sourceWidth = $Target.Width / $ratio
    $sourceHeight = $Target.Height / $ratio
    $sourceX = ($Image.Width - $sourceWidth) / 2.0
    $sourceY = ($Image.Height - $sourceHeight) / 2.0
    $source = New-Object System.Drawing.RectangleF($sourceX, $sourceY, $sourceWidth, $sourceHeight)
    $Graphics.DrawImage($Image, $Target, $source, [System.Drawing.GraphicsUnit]::Pixel)
}

function Write-PdfImage($Bitmap, [string]$Path, [double]$WidthIn, [double]$HeightIn) {
    $jpegStream = New-Object System.IO.MemoryStream
    $jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' } | Select-Object -First 1
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]95)
    $Bitmap.Save($jpegStream, $jpegCodec, $encoderParams)
    $jpegBytes = $jpegStream.ToArray()
    $jpegStream.Dispose()
    $encoderParams.Dispose()

    $ascii = [System.Text.Encoding]::ASCII
    $stream = New-Object System.IO.MemoryStream
    function Write-Ascii([string]$Value) {
        $bytes = $ascii.GetBytes($Value)
        $stream.Write($bytes, 0, $bytes.Length)
    }

    Write-Ascii "%PDF-1.4`n%1234`n"
    $offsets = New-Object System.Collections.Generic.List[long]

    $offsets.Add($stream.Position)
    Write-Ascii "1 0 obj`n<< /Type /Catalog /Pages 2 0 R >>`nendobj`n"
    $offsets.Add($stream.Position)
    Write-Ascii "2 0 obj`n<< /Type /Pages /Kids [3 0 R] /Count 1 >>`nendobj`n"

    $widthPt = ($WidthIn * 72).ToString('0.###', [Globalization.CultureInfo]::InvariantCulture)
    $heightPt = ($HeightIn * 72).ToString('0.###', [Globalization.CultureInfo]::InvariantCulture)
    $offsets.Add($stream.Position)
    Write-Ascii "3 0 obj`n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 $widthPt $heightPt] /Resources << /XObject << /Im0 5 0 R >> >> /Contents 4 0 R >>`nendobj`n"

    $content = "q`n$widthPt 0 0 $heightPt 0 0 cm`n/Im0 Do`nQ`n"
    $contentBytes = $ascii.GetBytes($content)
    $offsets.Add($stream.Position)
    Write-Ascii "4 0 obj`n<< /Length $($contentBytes.Length) >>`nstream`n"
    $stream.Write($contentBytes, 0, $contentBytes.Length)
    Write-Ascii "endstream`nendobj`n"

    $offsets.Add($stream.Position)
    Write-Ascii "5 0 obj`n<< /Type /XObject /Subtype /Image /Width $($Bitmap.Width) /Height $($Bitmap.Height) /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length $($jpegBytes.Length) >>`nstream`n"
    $stream.Write($jpegBytes, 0, $jpegBytes.Length)
    Write-Ascii "`nendstream`nendobj`n"

    $xrefOffset = $stream.Position
    Write-Ascii "xref`n0 6`n0000000000 65535 f `n"
    foreach ($offset in $offsets) {
        Write-Ascii ($offset.ToString('0000000000') + " 00000 n `n")
    }
    Write-Ascii "trailer`n<< /Size 6 /Root 1 0 R >>`nstartxref`n$xrefOffset`n%%EOF`n"
    [System.IO.File]::WriteAllBytes($Path, $stream.ToArray())
    $stream.Dispose()
}

$cfg = Get-Content -Raw -LiteralPath $ConfigPath | ConvertFrom-Json
$folder = $cfg.book_folder
$trimWidth = [double]$cfg.trim_width_in
$trimHeight = [double]$cfg.trim_height_in
$pages = [int]$cfg.page_count
$spineIn = $pages * $PaperThickness[[string]$cfg.paper]
$fullWidthIn = $BleedIn + $trimWidth + $spineIn + $trimWidth + $BleedIn
$fullHeightIn = $trimHeight + (2 * $BleedIn)
$width = Convert-InchesToPixels $fullWidthIn
$height = Convert-InchesToPixels $fullHeightIn
$spinePixels = Convert-InchesToPixels $spineIn
$spineX = Convert-InchesToPixels ($BleedIn + $trimWidth)
$frontX = $spineX + $spinePixels
$frontWidth = $width - $frontX

Write-Output ('KDP wrap dimensions: {0:F3} x {1:F3} in  ({2} x {3} px @ {4} DPI); spine {5:F3} in ({6} px)' -f $fullWidthIn, $fullHeightIn, $width, $height, $Dpi, $spineIn, $spinePixels)

$teal = Convert-HexColor ([string]$cfg.spine_color)
$accent = Convert-HexColor ([string]$cfg.accent_color)
$canvas = New-Object System.Drawing.Bitmap($width, $height, [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
$canvas.SetResolution($Dpi, $Dpi)
$graphics = [System.Drawing.Graphics]::FromImage($canvas)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
$graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$graphics.Clear($teal)

$artPath = Join-Path $folder ([string]$cfg.front_art)
$art = [System.Drawing.Image]::FromFile($artPath)
Draw-CoverFit $graphics $art (New-Object System.Drawing.Rectangle($frontX, 0, $frontWidth, $height))
$art.Dispose()

$safeWidth = $frontWidth - (Convert-InchesToPixels 1.0)
$titleFit = Get-FittedTitle $graphics ([string]$cfg.title).ToUpperInvariant() $safeWidth $trimWidth
$titleFont = $titleFit.Font
$titleLines = $titleFit.Lines
$titlePt = $titleFit.PointSize
$lineHeight = [int]($titleFont.Size * 1.14)
$subtitleFont = New-CoverFont ([Math]::Max((Convert-InchesToPixels 0.16), [int]($titleFont.Size * 0.30))) $false
$authorFont = New-CoverFont (Convert-InchesToPixels 0.26) $true
$subtitleLines = Get-WrappedLines $graphics ([string]$cfg.subtitle) $subtitleFont $safeWidth
if ($subtitleLines.Count -gt 3) { $subtitleLines = $subtitleLines[0..2] }
$subtitleHeight = [int]($subtitleFont.Size * 1.3)
$padding = Convert-InchesToPixels 0.25
$subtitleBlock = if ($subtitleLines.Count -gt 0) { ($subtitleLines.Count * $subtitleHeight) + (Convert-InchesToPixels 0.10) } else { 0 }
$bandHeight = $padding + ($titleLines.Count * $lineHeight) + $subtitleBlock + $padding
Write-Output ('title: {0} pt across {1} line(s)' -f $titlePt, $titleLines.Count)

$bandY = Convert-InchesToPixels 0.6
$bandBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(216, $teal.R, $teal.G, $teal.B))
$graphics.FillRectangle($bandBrush, $frontX, $bandY, $frontWidth, $bandHeight)
$bandBrush.Dispose()

$whiteBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$subtitleBrush = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 240, 235))
$centerX = $frontX + ($frontWidth / 2.0)
$y = $bandY + $padding
foreach ($line in $titleLines) {
    $lineWidth = Measure-TextWidth $graphics $line $titleFont
    $graphics.DrawString($line, $titleFont, $whiteBrush, [single]($centerX - ($lineWidth / 2.0)), [single]$y, [System.Drawing.StringFormat]::GenericTypographic)
    $y += $lineHeight
}
if ($subtitleLines.Count -gt 0) {
    $y += Convert-InchesToPixels 0.10
    foreach ($line in $subtitleLines) {
        $lineWidth = Measure-TextWidth $graphics $line $subtitleFont
        $graphics.DrawString($line, $subtitleFont, $subtitleBrush, [single]($centerX - ($lineWidth / 2.0)), [single]$y, [System.Drawing.StringFormat]::GenericTypographic)
        $y += $subtitleHeight
    }
}

$authorBandHeight = Convert-InchesToPixels 0.7
$authorBandY = $height - (Convert-InchesToPixels 0.5) - $authorBandHeight
$accentBrush = New-Object System.Drawing.SolidBrush($accent)
$graphics.FillRectangle($accentBrush, $frontX, $authorBandY, $frontWidth, $authorBandHeight)
$authorText = [string]$cfg.author
$authorWidth = Measure-TextWidth $graphics $authorText $authorFont
$graphics.DrawString($authorText, $authorFont, $whiteBrush, [single]($centerX - ($authorWidth / 2.0)), [single]($authorBandY + (Convert-InchesToPixels 0.18)), [System.Drawing.StringFormat]::GenericTypographic)

$backHeadlineFont = New-CoverFont (Convert-InchesToPixels 0.22) $true
$backFont = New-CoverFont (Convert-InchesToPixels 0.155) $false
$backX = Convert-InchesToPixels 0.95
$backY = Convert-InchesToPixels 1.2
$backSafeWidth = $spineX - (Convert-InchesToPixels 1.9)
foreach ($line in (Get-WrappedLines $graphics ([string]$cfg.back_headline) $backHeadlineFont $backSafeWidth)) {
    $graphics.DrawString($line, $backHeadlineFont, $accentBrush, [single]$backX, [single]$backY, [System.Drawing.StringFormat]::GenericTypographic)
    $backY += Convert-InchesToPixels 0.28
}
$backY += Convert-InchesToPixels 0.15
foreach ($paragraph in (([string]$cfg.back_text) -split "`n")) {
    foreach ($line in (Get-WrappedLines $graphics $paragraph $backFont $backSafeWidth)) {
        $graphics.DrawString($line, $backFont, $whiteBrush, [single]$backX, [single]$backY, [System.Drawing.StringFormat]::GenericTypographic)
        $backY += Convert-InchesToPixels 0.21
    }
    $backY += Convert-InchesToPixels 0.12
}

$barcodeWidth = Convert-InchesToPixels 2.0
$barcodeHeight = Convert-InchesToPixels 1.2
$barcodeRight = $spineX - (Convert-InchesToPixels 0.25)
$barcodeBottom = $height - (Convert-InchesToPixels $BleedIn) - (Convert-InchesToPixels 0.25)
$graphics.FillRectangle($whiteBrush, $barcodeRight - $barcodeWidth, $barcodeBottom - $barcodeHeight, $barcodeWidth, $barcodeHeight)

$graphics.FillRectangle((New-Object System.Drawing.SolidBrush($teal)), $spineX, 0, $spinePixels, $height)
if (($pages -ge 79) -and ($spineIn -ge 0.25)) {
    $spineFont = New-CoverFont ([Math]::Min((Convert-InchesToPixels 0.16), [int]($spinePixels * 0.55))) $true
    $spineText = ([string]$cfg.title) + '   -   ' + ([string]$cfg.author)
    $spineTemp = New-Object System.Drawing.Bitmap((Convert-InchesToPixels ($trimHeight - 1.0)), $spinePixels, [System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
    $spineGraphics = [System.Drawing.Graphics]::FromImage($spineTemp)
    $spineGraphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $spineWidth = Measure-TextWidth $spineGraphics $spineText $spineFont
    $spineGraphics.DrawString($spineText, $spineFont, $whiteBrush, [single](($spineTemp.Width - $spineWidth) / 2.0), [single](($spinePixels - $spineFont.Size) / 2.0 - (Convert-InchesToPixels 0.01)), [System.Drawing.StringFormat]::GenericTypographic)
    $spineGraphics.Dispose()
    $spineTemp.RotateFlip([System.Drawing.RotateFlipType]::Rotate270FlipNone)
    $graphics.DrawImageUnscaled($spineTemp, $spineX, [int](($height - $spineTemp.Height) / 2))
    $spineTemp.Dispose()
    $spineFont.Dispose()
}

$prefix = if ($cfg.output_prefix) { [string]$cfg.output_prefix } else { 'Cover' }
$pngPath = Join-Path $folder ($prefix + '_WRAP.png')
$pdfPath = Join-Path $folder ($prefix + '_WRAP.pdf')
$graphics.Dispose()
$canvas.Save($pngPath, [System.Drawing.Imaging.ImageFormat]::Png)
Write-PdfImage $canvas $pdfPath $fullWidthIn $fullHeightIn
$canvas.Dispose()

$titleFont.Dispose()
$subtitleFont.Dispose()
$authorFont.Dispose()
$backHeadlineFont.Dispose()
$backFont.Dispose()
$whiteBrush.Dispose()
$subtitleBrush.Dispose()
$accentBrush.Dispose()

Write-Output ('saved ' + $pngPath)
Write-Output ('saved ' + $pdfPath)
