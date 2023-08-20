# GENERAL
alias mpv='devour mpv'
alias openvpn='sudo openvpn'
alias scrcpy='devour scrcpy'
alias zathura='devour zathura'

# PYTHON
alias py='python'
alias pi='pip install'
alias cvenv='python -m venv'
alias server='python -m http.server'
alias venv='source ./venv/bin/activate.fish'
alias cpc='find . -name "__pycache__" -exec rm -rf {} \;'

# FILE/FOLDER MANAGING
alias root='cd ~/'
alias md='mkdir'
alias rd='rm -rf'
alias rm='rm -i'
alias edit='vim'
alias rename='mv'
alias new='touch'
alias clr='clear'
alias cls='clear'

# SYSTEM RELATED
alias vialias='vim ~/.bash_aliases'
alias showalias='cat ~/.bash_aliases'

# GIT
alias clone='git clone'
alias add='git add --all'
alias com='git commit -m'
alias comrnd='git commit -m "$(curl -s https://whatthecommit.com/index.txt)"'
alias cam='git commit --amend'
alias remote='git remote add origin'
alias push='git push -u origin master'
alias pull='git pull origin master'
alias rebase='git rebase origin/master'
alias fetch='git fetch --all --prune --verbose --progress'
alias branch='git checkout -b'
alias diff='git diff'
alias gst='git status'
alias gstr='git remote update && git status'
alias log='git log --pretty=oneline'
