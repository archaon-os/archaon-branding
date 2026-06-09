# archaon-branding 🐦‍⬛

> The visual identity and dotfiles for Archaon OS.

This repository contains all branding assets, dotfiles, and default configurations for Archaon OS.

---

## Contents

    archaon-branding/
    ├── dotfiles/
    │   ├── hypr/
    │   │   ├── hyprland.conf
    │   │   ├── hyprlock.conf
    │   │   ├── hypridle.conf
    │   │   └── hyprpaper.conf
    │   ├── waybar/
    │   │   ├── config.jsonc
    │   │   └── style.css
    │   ├── wofi/
    │   │   ├── config
    │   │   └── style.css
    │   ├── mako/
    │   │   └── config
    │   ├── kitty/
    │   │   └── kitty.conf
    │   ├── fastfetch/
    │   │   ├── config.jsonc
    │   │   └── archaon.txt
    │   ├── oh-my-posh/
    │   │   └── archaon.omp.json
    │   └── .zshrc
    └── wallpaper.png

---

## Using the Dotfiles

Copy configs to your home directory:

    git clone https://github.com/archaon-os/archaon-branding.git
    cd archaon-branding
    cp -r dotfiles/hypr ~/.config/
    cp -r dotfiles/waybar ~/.config/
    cp -r dotfiles/wofi ~/.config/
    cp -r dotfiles/mako ~/.config/
    cp -r dotfiles/kitty ~/.config/
    cp -r dotfiles/fastfetch ~/.config/
    cp -r dotfiles/oh-my-posh ~/.config/
    cp dotfiles/.zshrc ~/

---

## Color Palette

| Name | Hex | Usage |
|------|-----|-------|
| Background | `#000000` | Pure black base |
| Neon Green | `#00ff88` | Primary accent |
| Neon Blue | `#00ccff` | Secondary accent |
| Dark Surface | `#0a0a0a` | Panels, bars |
| Red Accent | `#ff0055` | Errors, urgent |
| Yellow Accent | `#ffaa00` | Warnings |

---

## Stack

| Component | Choice |
|-----------|--------|
| WM | Hyprland |
| Bar | Waybar |
| Launcher | Wofi |
| Terminal | Kitty |
| Shell | ZSH + oh-my-posh |
| Notifications | Mako |
| Fetch | Fastfetch |

---

## Design Philosophy

- Arcane / mystical aesthetic
- Pure black base
- Neon green and blue accents
- Sharp geometric identity
- Minimal but expressive

---

## Related Repos

| Repo | Purpose |
|------|---------|
| [archaon-os](https://github.com/archaon-os/archaon-os) | Main repo |
| [archaon-iso](https://github.com/archaon-os/archaon-iso) | ISO build |
| [archaon-aon](https://github.com/archaon-os/archaon-aon) | Package manager |

---

## License

GPL v3 — see LICENSE file.

---

**Archaon OS — 1.0.0 "Chaotic Crow" 🐦‍⬛**
