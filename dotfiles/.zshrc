# Archaon OS - ZSH Config

HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history
setopt appendhistory sharehistory incappendhistory

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

eval "$(oh-my-posh init zsh --config ~/.config/oh-my-posh/archaon.omp.json)"

alias ls='ls --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias grep='grep --color=auto'
alias vim='nvim'
alias vi='nvim'
alias top='btop'
alias update='sudo pacman -Syu'
alias yayup='yay -Syu'
alias cls='clear'
alias ..='cd ..'
alias ...='cd ../..'
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline --graph'
alias lg='lazygit'
alias dk='docker'
alias dkc='docker-compose'
alias yins='yay -S'
alias yrm='yay -Rns'
alias ysearch='yay -Ss'

fastfetch

source /usr/share/fzf/key-bindings.zsh 2>/dev/null
source /usr/share/fzf/completion.zsh 2>/dev/null

autoload -Uz compinit && compinit
zstyle ':completion:*' menu select
