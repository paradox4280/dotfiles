local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath("data").."/site/pack/packer/start/packer.nvim"
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({"git", "clone", "--depth", "1", "https://github.com/wbthomason/packer.nvim", install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins-setup.lua source <afile> | PackerSync
  augroup end
]])

return require('packer').startup(function(use)
  use "jiangmiao/auto-pairs"
  use "numToStr/Comment.nvim"
  use "wakatime/vim-wakatime"
  use "wbthomason/packer.nvim"
  use "nvim-tree/nvim-tree.lua"
  use "vim-airline/vim-airline"
  use "norcalli/nvim-colorizer.lua"
  use "kyazdani42/nvim-web-devicons"

  -- Fuzzy finding
  use {
      "nvim-telescope/telescope.nvim", branch = "0.1.x",
      requires = { {"nvim-lua/plenary.nvim"} }
  }
  use { "nvim-telescope/telescope-fzf-native.nvim", run = "make" }

  -- autocompletion
  use "hrsh7th/nvim-cmp" -- completion plugin
  use "hrsh7th/cmp-buffer" -- source for text in buffer
  use "hrsh7th/cmp-path" -- source for file system paths

  -- snippets
  use "L3MON4D3/LuaSnip" -- snippet engine
  use "saadparwaiz1/cmp_luasnip" -- for autocompletion
  use "rafamadriz/friendly-snippets" -- useful snippets

  -- treesitter
  use {
      "nvim-treesitter/nvim-treesitter",
      run = function ()
        require("nvim-treesitter.install").update({ with_sync = true })
      end
  }

  -- managing & installing lsp servers, linters & formatters
  use {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
      "neovim/nvim-lspconfig",
      "hrsh7th/cmp-nvim-lsp"
  }
  use { "glepnir/lspsaga.nvim", branch = "main" }

  use "onsails/lspkind.nvim" -- vs-code like icons for autocompletion

  -- git integration
  use "lewis6991/gitsigns.nvim" -- show line modifications on left hand side

  -- Colorscheme
  use { "ellisonleao/gruvbox.nvim" }
  use { "catppuccin/nvim", as = "catppuccin" }
  use { "vim-airline/vim-airline-themes" }

  if packer_bootstrap then
    require('packer').sync()
  end
end)
