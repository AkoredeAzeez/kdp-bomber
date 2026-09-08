#!/usr/bin/env python3
r"""Instructional graphics for GENIE_INSTALLATION_GUIDE (operator directive
2026-08-30): mock terminal / File Explorer windows with plain-English callouts,
drawn with PIL so they are crisp, consistent, and rebuildable. Output:
Genie/guide_images/*.png. Rerun any time; then rebuild the guide PDF."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "guide_images")
os.makedirs(OUT, exist_ok=True)

MONO = "consola.ttf"
SANS = "segoeui.ttf"
SANSB = "segoeuib.ttf"

def font(name, size):
    try:
        return ImageFont.truetype(name, size)
    except Exception:
        return ImageFont.load_default()

F_TITLE = font(SANS, 22)
F_TERM = font(MONO, 26)
F_NOTE = font(SANSB, 26)
F_SMALL = font(SANS, 22)

INK = (40, 44, 52)
ORANGE = (200, 106, 30)
TEAL = (31, 78, 95)
TERM_BG = (18, 18, 22)
TERM_TXT = (222, 222, 222)
PROMPT = (120, 200, 255)
CMD = (255, 255, 160)

def window(draw, x, y, w, h, title):
    draw.rounded_rectangle([x, y, x + w, y + h], 12, fill=TERM_BG, outline=(90, 90, 96), width=2)
    draw.rectangle([x, y, x + w, y + 44], fill=(46, 48, 56))
    draw.rounded_rectangle([x, y, x + w, y + 60], 12, outline=(90, 90, 96), width=2)
    draw.rectangle([x + 2, y + 44, x + w - 2, y + 62], fill=TERM_BG)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        draw.ellipse([x + 18 + i * 34, y + 13, x + 36 + i * 34, y + 31], fill=c)
    draw.text((x + 130, y + 9), title, font=F_TITLE, fill=(200, 200, 205))

def note(draw, x, y, text, w=None):
    draw.text((x, y), text, font=F_NOTE, fill=ORANGE)

def arrow(draw, x0, y0, x1, y1):
    draw.line([x0, y0, x1, y1], fill=ORANGE, width=5)
    import math
    ang = math.atan2(y1 - y0, x1 - x0)
    for da in (0.5, -0.5):
        draw.line([x1, y1, x1 - 22 * math.cos(ang - da), y1 - 22 * math.sin(ang - da)],
                  fill=ORANGE, width=5)

# ---- 1. Opening a terminal from the File Explorer address bar ---------------
img = Image.new("RGB", (1400, 560), (250, 250, 248))
d = ImageDraw.Draw(img)
d.rounded_rectangle([40, 40, 1360, 200], 12, fill=(255, 255, 255), outline=(150, 150, 155), width=2)
d.rectangle([40, 40, 1360, 92], fill=(238, 240, 244))
d.text((70, 52), "File Explorer  -  your extracted Genie folder", font=F_TITLE, fill=INK)
d.rounded_rectangle([70, 112, 1330, 168], 8, fill=(255, 255, 255), outline=TEAL, width=3)
d.text((92, 124), "cmd", font=F_TERM, fill=INK)
d.rectangle([176, 122, 180, 160], fill=INK)  # text cursor
note(d, 90, 250, "1. Click INSIDE the address bar (the long box at the top).")
note(d, 90, 300, "2. The folder path highlights. Type the three letters:  cmd")
note(d, 90, 350, "3. Press Enter. A black window opens: that is your terminal,")
note(d, 90, 400, "    already pointed at this folder. Nothing to find or configure.")
arrow(d, 320, 255, 220, 175)
img.save(os.path.join(OUT, "explorer_cmd.png"))

# ---- 2. Terminal basics: the prompt shows where you are ---------------------
img = Image.new("RGB", (1400, 620), (250, 250, 248))
d = ImageDraw.Draw(img)
window(d, 40, 40, 1320, 320, "Command Prompt")
d.text((70, 120), "C:\\Users\\you\\Downloads\\Genie_Community>", font=F_TERM, fill=PROMPT)
d.text((70, 170), "C:\\Users\\you\\Downloads\\Genie_Community> python genie_bootstrap.py",
       font=F_TERM, fill=TERM_TXT)
d.text((70, 220), "[env] environment ready.", font=F_TERM, fill=(150, 220, 150))
arrow(d, 420, 430, 330, 145)
note(d, 440, 415, "This line is the PROMPT. It always shows the folder")
note(d, 440, 455, "you are standing in. You type after the > sign.")
note(d, 90, 520, "Type a command, press Enter, and the terminal answers on the next line.")
img.save(os.path.join(OUT, "terminal_prompt.png"))

# ---- 3. cd: moving between folders ------------------------------------------
img = Image.new("RGB", (1400, 800), (250, 250, 248))
d = ImageDraw.Draw(img)
window(d, 40, 40, 1320, 420, "Command Prompt")
d.text((70, 120), "C:\\Users\\you> ", font=F_TERM, fill=PROMPT)
d.text((70 + 15.6 * 14, 120), "cd Genie", font=F_TERM, fill=CMD)
d.text((70, 170), "C:\\Users\\you\\Genie>", font=F_TERM, fill=PROMPT)
d.text((70, 250), "C:\\Users\\you\\Genie> ", font=F_TERM, fill=PROMPT)
d.text((70 + 15.6 * 21, 250), "cd ..", font=F_TERM, fill=CMD)
d.text((70, 300), "C:\\Users\\you>", font=F_TERM, fill=PROMPT)
note(d, 90, 520, "cd means 'change directory': it moves you INTO a folder.")
note(d, 90, 570, "After  cd Genie  the prompt shows \\Genie: you are inside it.")
note(d, 90, 645, "cd ..  (cd, space, two dots) steps back OUT to the")
note(d, 90, 695, "previous folder. Those two moves are all you ever need.")
img.save(os.path.join(OUT, "terminal_cd.png"))

# ---- 4. The drag trick: cd + drag the folder --------------------------------
img = Image.new("RGB", (1400, 760), (250, 250, 248))
d = ImageDraw.Draw(img)
window(d, 40, 250, 1320, 260, "Command Prompt")
d.text((70, 330), "C:\\Users\\you> ", font=F_TERM, fill=PROMPT)
d.text((70 + 15.6 * 14, 330), "cd C:\\Users\\you\\Documents\\Genie", font=F_TERM, fill=CMD)
d.text((70, 380), "C:\\Users\\you\\Documents\\Genie>", font=F_TERM, fill=PROMPT)
# folder icon
fx, fy = 240, 70
d.rounded_rectangle([fx, fy + 14, fx + 120, fy + 96], 8, fill=(255, 202, 40), outline=(200, 150, 20), width=3)
d.rounded_rectangle([fx, fy, fx + 56, fy + 30], 6, fill=(255, 202, 40), outline=(200, 150, 20), width=3)
d.text((fx - 30, fy + 104), "your Genie folder", font=F_SMALL, fill=INK)
arrow(d, fx + 130, fy + 70, 520, 335)
note(d, 560, 60, "Can't type the path? Type  cd  and ONE SPACE,")
note(d, 560, 110, "then DRAG the folder from Explorer into the")
note(d, 560, 160, "black window. The full path types itself.")
note(d, 560, 210, "Then press Enter.")
note(d, 90, 570, "Works on Mac too: type  cd  and a space in Terminal, drag the folder in,")
note(d, 90, 620, "press Return. The prompt then shows you are inside that folder.")
img.save(os.path.join(OUT, "terminal_drag.png"))

print("wrote 4 images to", OUT)
