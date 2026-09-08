FROM node:20-bookworm-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    HOME=/data/home

# python (Genie's own scripts), git, LibreOffice (DOCX -> PDF conversion,
# same role Word/LibreOffice play on the operator's machine), fontconfig so
# LibreOffice can find and embed the packaged fonts when rendering PDFs.
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip python3-venv \
        git curl ca-certificates \
        libreoffice-writer libreoffice-core \
        fontconfig \
    && rm -rf /var/lib/apt/lists/*

# Pinned to the version this Dockerfile was written against. Bump deliberately.
RUN npm install -g @anthropic-ai/claude-code@2.1.263

WORKDIR /app
COPY . /app

RUN mkdir -p /usr/share/fonts/truetype/genie \
    && cp /app/*.ttf /usr/share/fonts/truetype/genie/ \
    && fc-cache -f

RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt
ENV PATH="/opt/venv/bin:${PATH}"

RUN chmod +x /app/deploy/entrypoint.sh

ENTRYPOINT ["/app/deploy/entrypoint.sh"]
