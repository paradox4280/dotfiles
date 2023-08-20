#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# NVM
if [ -f /usr/share/nvm/init-nvm.sh ]; then
    . /usr/share/nvm/init-nvm.sh
fi

# User-defined aliases
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
