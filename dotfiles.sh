#!/bin/bash
# archaon-dotfiles bootstrap
# curl -fsSL https://raw.githubusercontent.com/archaon-os/archaon-branding/main/dotfiles.sh | bash

GREEN='\033[38;2;0;255;136m'
BLUE='\033[38;2;0;204;255m'
DIM='\033[38;2;51;51;51m'
RED='\033[38;2;255;0;85m'
RESET='\033[0m'
BOLD='\033[1m'

crow_log() {
    echo -e "${BLUE}  🐦‍⬛  $1${RESET}"
    sleep 0.6
}

success() {
    echo -e "${GREEN}  ✓  $1${RESET}"
}

error() {
    echo -e "${RED}  ✗  $1${RESET}"
    exit 1
}

echo -e "${GREEN}"
echo "        /\\"
echo "       /  \\"
echo "      / /\\ \\"
echo "     / /  \\ \\"
echo "    / / /\\ \\ \\"
echo "   /_/ /__\\ \\_\\"
echo -e "${BLUE}      /\\  /\\"
echo "     /  \\/  \\"
echo "     \\  /\\  /"
echo -e "      \\/  \\/${RESET}"
echo ""
echo -e "  ${GREEN}${BOLD}A R C H A O N  O S${RESET}"
echo -e "  ${BLUE}Dotfiles Installer v0.1.0 — Chaotic Crow 🐦‍⬛${RESET}"
echo ""

# ─────────────────────────────────────────
# CHECK ROOT
# ─────────────────────────────────────────

if [ "$EUID" -ne 0 ]; then
    error "Please run as root: sudo bash dotfiles.sh"
fi

# ─────────────────────────────────────────
# INSTALL DEPS
# ─────────────────────────────────────────

crow_log "Checking Python..."
if ! command -v python3 &>/dev/null; then
    crow_log "Installing Python..."
    if command -v pacman &>/dev/null; then
        pacman -S --noconfirm python python-pip
    elif command -v apt &>/dev/null; then
        apt-get install -y python3 python3-pip
    fi
fi
success "Python ready"

crow_log "Installing pyfiglet..."
python3 -m pip install pyfiglet --break-system-packages -q 2>/dev/null || \
python3 -m pip install pyfiglet -q 2>/dev/null
success "pyfiglet ready"

crow_log "Checking git..."
if ! command -v git &>/dev/null; then
    crow_log "Installing git..."
    if command -v pacman &>/dev/null; then
        pacman -S --noconfirm git
    elif command -v apt &>/dev/null; then
        apt-get install -y git
    fi
fi
success "git ready"

# ─────────────────────────────────────────
# DOWNLOAD AND RUN
# ─────────────────────────────────────────

crow_log "Downloading dotfiles installer..."
curl -fsSL https://raw.githubusercontent.com/archaon-os/archaon-branding/main/archaon-dotfiles.py \
    -o /tmp/archaon-dotfiles.py || error "Failed to download installer"

success "Downloaded"
crow_log "Launching dotfiles installer..."
sleep 0.5

python3 /tmp/archaon-dotfiles.py
rm -f /tmp/archaon-dotfiles.py
