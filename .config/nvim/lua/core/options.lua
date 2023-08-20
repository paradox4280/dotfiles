local opt = vim.opt

-- Show line numbers
opt.relativenumber = true
opt.number = true

-- Show line cursor
opt.cursorline = true

-- Show file stats
opt.ruler = true

-- Blink cursor on error instead of beeping (grr)
opt.visualbell = true

-- Encoding
opt.encoding = "utf-8"

-- Case insensitive search
opt.ignorecase = true
opt.smartcase = true

-- Tabs & indentation
opt.tabstop = 4
opt.shiftwidth = 4
opt.softtabstop = 4
opt.expandtab = true
opt.autoindent = true

-- Line wrapping
opt.wrap = false

-- Appearance
opt.termguicolors = true
opt.background = "dark"
-- opt.signcolumn = "yes"

-- Backspace
opt.backspace = "indent,eol,start"

-- Clipboard
opt.clipboard:append("unnamedplus")

-- Split windows
opt.splitright = true
opt.splitbelow = true

opt.iskeyword:append("-")

-- Allow hidden buffers
opt.hidden = true

-- Rendering
opt.ttyfast = true

-- Status bar
opt.laststatus = 2

-- Last line
opt.showmode = true
opt.showcmd = true

-- Cursor motion
opt.scrolloff = 3
