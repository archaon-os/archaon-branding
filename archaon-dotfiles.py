#!/usr/bin/env python3
"""
archaon-dotfiles
Version: 0.1.0 "Chaotic Crow"
Archaon OS Dotfiles Installer
"""

import os
import sys
import time
import random
import subprocess
import shutil
from pathlib import Path

import pyfiglet

GREEN = '\033[38;2;0;255;136m'
BLUE = '\033[38;2;0;204;255m'
DIM = '\033[38;2;51;51;51m'
RED = '\033[38;2;255;0;85m'
YELLOW = '\033[38;2;255;170;0m'
RESET = '\033[0m'
BOLD = '\033[1m'

GLITCH = ['░', '▒', '▓', '█', '▄', '▀', '■', '●']

def get_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except:
        return 120, 40

def run(cmd, capture=False):
    if capture:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()
    return subprocess.call(cmd, shell=True)

def crow_log(msg):
    cols, _ = get_terminal_size()
    print(' ' * ((cols - 60) // 2) + BLUE + f"  🐦‍⬛  {msg}" + RESET)
    time.sleep(0.3)

def success(msg):
    cols, _ = get_terminal_size()
    print(' ' * ((cols - 60) // 2) + GREEN + f"  ✓  {msg}" + RESET)

def error(msg):
    cols, _ = get_terminal_size()
    print(' ' * ((cols - 60) // 2) + RED + f"  ✗  {msg}" + RESET)

def section(title):
    cols, _ = get_terminal_size()
    print()
    print(' ' * ((cols - 60) // 2) + BLUE + BOLD + f"── {title} ──" + RESET)
    print()

def get_logo(word='ARCHAON'):
    text = pyfiglet.figlet_format(word, font='colossal')
    lines = text.split('\n')
    max_len = max(len(l) for l in lines)
    result = []
    for i, line in enumerate(lines):
        padded = line.ljust(max_len + 2)
        new_line = ''
        for j, ch in enumerate(padded):
            if ch != ' ':
                new_line += ch
            else:
                if i > 0 and j > 0 and j-1 < len(lines[i-1]) and lines[i-1][j-1] != ' ':
                    new_line += '░'
                else:
                    new_line += ' '
        result.append(new_line)
    return result

def welcome_animation():
    logo = get_logo('ARCHAON')
    cols, rows = get_terminal_size()
    logo_height = len(logo)
    logo_width = max(len(l) for l in logo)
    left_pad = max(0, (cols - logo_width) // 2)

    line_pos = []
    line_speed = []
    for i in range(logo_height):
        line_pos.append(-(logo_height - i) - random.randint(0, 8))
        line_speed.append(round(random.uniform(0.3, 0.9), 1))

    final_top = max(0, (rows - logo_height - 6) // 2)
    final_positions = [final_top + i for i in range(logo_height)]
    landed = [False] * logo_height

    while not all(landed):
        os.system('clear')
        for i in range(logo_height):
            if not landed[i]:
                line_pos[i] += line_speed[i]
                if line_pos[i] >= final_positions[i]:
                    line_pos[i] = final_positions[i]
                    landed[i] = True

        frame_lines = {}
        for i in range(logo_height):
            y = int(line_pos[i])
            if y >= 0:
                frame_lines[y] = (logo[i], landed[i])

        for y in range(rows - 4):
            if y in frame_lines:
                line, is_landed = frame_lines[y]
                out = ' ' * left_pad
                for ch in line:
                    if ch == '░':
                        out += BLUE + ch + RESET
                    elif ch != ' ':
                        out += (GREEN if is_landed else YELLOW) + ch + RESET
                    else:
                        out += ' '
                print(out)
            else:
                print()
        time.sleep(0.04)

    subtitle = "Archaon OS — Dotfiles Installer 🐦‍⬛"
    sub2 = "v0.1.0 Chaotic Crow"
    print()
    print(' ' * ((cols - len(subtitle)) // 2) + GREEN + BOLD + subtitle + RESET)
    print(' ' * ((cols - len(sub2)) // 2) + BLUE + sub2 + RESET)
    print()
    time.sleep(1.5)

def get_username():
    user = run("logname 2>/dev/null || whoami", capture=True)
    if user == "root":
        user = run("ls /home | head -1", capture=True)
    return user.strip()

def backup_existing(home):
    backup_dir = Path(home) / ".config-backup-archaon"
    if Path(f"{home}/.config/hypr").exists():
        section("Backing up existing configs")
        crow_log(f"Backing up to {backup_dir}...")
        backup_dir.mkdir(parents=True, exist_ok=True)
        dirs = ["hypr", "waybar", "wofi", "mako", "kitty", "fastfetch", "oh-my-posh"]
        for d in dirs:
            src = Path(f"{home}/.config/{d}")
            if src.exists():
                shutil.copytree(src, backup_dir / d, dirs_exist_ok=True)
        success(f"Backup saved to {backup_dir}")

def apply_dotfiles(username):
    home = f"/home/{username}"
    config = f"{home}/.config"

    section("Pulling Dotfiles")
    crow_log("Cloning archaon-branding...")
    run("rm -rf /tmp/archaon-branding")
    run("git clone https://github.com/archaon-os/archaon-branding.git /tmp/archaon-branding")
    success("Repo cloned")

    backup_existing(home)

    section("Applying Dotfiles")

    dirs = ["hypr", "waybar", "wofi", "mako", "kitty", "fastfetch", "oh-my-posh", "gtk-3.0", "gtk-4.0"]
    for d in dirs:
        src = f"/tmp/archaon-branding/dotfiles/{d}"
        dst = f"{config}/{d}"
        if Path(src).exists():
            crow_log(f"Applying {d}...")
            run(f"rm -rf {dst}")
            run(f"cp -r {src} {dst}")
            success(f"{d} applied")
        else:
            error(f"{d} not found in repo, skipping")

    crow_log("Applying .zshrc...")
    run(f"cp /tmp/archaon-branding/dotfiles/.zshrc {home}/.zshrc")
    success(".zshrc applied")

    section("Wallpaper")
    crow_log("Applying wallpaper...")
    run("mkdir -p /usr/share/archaon")
    run("cp /tmp/archaon-branding/wallpaper.png /usr/share/archaon/wallpaper.png")
    success("Wallpaper applied")

    section("Fixing Permissions")
    crow_log("Setting ownership...")
    run(f"chown -R {username}:{username} {config}")
    run(f"chown {username}:{username} {home}/.zshrc")
    success("Permissions fixed")

    run("rm -rf /tmp/archaon-branding")

def main():
    try:
        import pyfiglet
    except ImportError:
        subprocess.call("pip install pyfiglet --break-system-packages -q", shell=True)
        import pyfiglet

    welcome_animation()

    username = get_username()
    cols, _ = get_terminal_size()
    print(' ' * ((cols - 60) // 2) + BLUE + f"  Applying dotfiles for: {GREEN}{username}{RESET}")
    print()
    time.sleep(1)

    apply_dotfiles(username)

    print()
    cols, _ = get_terminal_size()
    print(' ' * ((cols - 60) // 2) + GREEN + BOLD + "✓ Dotfiles applied! 🐦‍⬛" + RESET)
    print(' ' * ((cols - 60) // 2) + BLUE + "Restart Hyprland to apply changes." + RESET)
    print(' ' * ((cols - 60) // 2) + DIM + "hyprctl reload" + RESET)
    print()

if __name__ == "__main__":
    main()
