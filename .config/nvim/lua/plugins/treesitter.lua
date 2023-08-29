local treesitter = require("nvim-treesitter.configs")

treesitter.setup({
    highlight = {
        enable = true
    },
    indent = { enable = true },
    autotag = { enable = true },
    ensure_installed = {
        "css",
        "vim",
        "lua",
        "bash",
        "json",
        "yaml",
        "html",
        "prisma",
        "python",
        "markdown",
        "gitignore",
        "javascript",
        "dockerfile",
        "markdown_inline"
    },
    auto_install = true,
})
