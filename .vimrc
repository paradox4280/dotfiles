" Map escape to jj
imap jj <Esc>

" TODO: Pick a leader key
" let mapleader = " "

" Don't try to be vi compatible
set nocompatible

" Helps force plugins to load correctly when it is turned back on below
filetype off

" TODO: Load plugins here (pathogen, vundle or vim-plug)
call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'

Plug 'lilydjwg/colorizer'

Plug 'preservim/nerdtree'

Plug 'jiangmiao/auto-pairs'

Plug 'tpope/vim-commentary'

Plug 'wakatime/vim-wakatime'

Plug 'ryanoasis/vim-devicons'

Plug 'vim-airline/vim-airline'

Plug 'vim-airline/vim-airline-themes'

Plug 'catppuccin/vim', { 'as': 'catppuccin' }

call plug#end()

" Comment line ctrl + /
nmap <C-_> <Plug>CommentaryLine
vmap <C-_> <Plug>CommentaryLine<CR>gv

" NerdTree
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

" Show hidden files in NerdTree
let NERDTreeShowHidden=1

" Air-line
let g:airline_powerline_fonts = 1

" Turn on syntax highlighting
syntax on

" For plugins to load correctly
filetype plugin indent on

" Security
set modelines=0

" Show line numbers
set number relativenumber

" Change curor by modes
let &t_SI = "\e[6 q"
let &t_EI = "\e[2 q"

"Ctrl+Shift+up move line above"
nmap <C-S-Up> :m -2<CR>

"Ctrl+Shift+down move line below
nmap <C-S-Down> :m +1<CR>

" Show line cursor
set cursorline

" Show file stats
set ruler

" Blink cursor on error instead of beeping (grr)
set visualbell

" Encoding
set encoding=utf-8

" Case insensitive search
set ignorecase
set smartcase

" Whitespace
set nowrap
set textwidth=79
set formatoptions=tcqrn1
set tabstop=2
set shiftwidth=2
set softtabstop=2
set expandtab
set noshiftround

" Cursor motion
set scrolloff=3
set backspace=indent,eol,start
set matchpairs+=<:> " use % to jump between pairs
runtime! macros/matchit.vim

" Move up/down editor lines
nnoremap j gj
nnoremap k gk

" Allow hidden buffers
set hidden

" Rendering
set ttyfast

" Status bar
set laststatus=2

" Last line
set showmode
set showcmd

" Remap help key.
inoremap <F1> <ESC>:set invfullscreen<CR>a
nnoremap <F1> :set invfullscreen<CR>
vnoremap <F1> :set invfullscreen<CR>

" Formatting
map <leader>q gqip

" Visualize tabs and newlines
set listchars=tab:▸\ ,eol:¬
" Uncomment this to enable by default:
" set list " To enable by default
" Or use your leader key + l to toggle on/off
map <leader>l :set list!<CR> " Toggle tabs and EOL

" Theme
set termguicolors
set background=dark
colorscheme gruvbox

" Force airline to use colorscheme
let g:airline_theme = 'base16_gruvbox_dark_hard'

" Trasparent
hi NonText ctermbg=none
hi Normal guibg=NONE ctermbg=NONE
