# Neovim Setup Documentation — Python Syntax Highlighting, LSP & Fuzzy Finding

**Environment:** WSL2 Ubuntu (`\\wsl.localhost\Ubuntu\home\filtz21`)
**Date:** 2026-07-16 (initial setup); updated 2026-07-16 (recurrence + diagnosis, §11); updated 2026-07-16 (Telescope + LSP + completion, §12–§17)
**Goal:** Get color-coded Python syntax highlighting working in Neovim using treesitter, then extend the same config with fuzzy finding (Telescope) and language-server features (LSP diagnostics, go-to-definition, completion) for Python and Lua.

---

## 1. Starting point

`nvim` was already installed (`/usr/bin/nvim`), but `~/.config/nvim` did not exist — there was no `init.lua`, so Neovim was running on defaults only.

```
filtz21@Panda2:~/.config$ ls -la
drwxr-x---  2 filtz21 filtz21 4096 envman
drwxr-xr-x  2 filtz21 filtz21 4096 go
drwxr-x--x  2 filtz21 filtz21 4096 gh
drwxr-xr-x  2 filtz21 filtz21 4096 ubuntu-insights
# (no nvim/ directory)
```

`~/.local/share/nvim` (plugin/data dir) already existed, confirming nvim had been run before — just never configured.

---

## 2. Config approach chosen

Two options were considered:

| Option | Highlighting quality | Setup cost |
|---|---|---|
| Built-in (`syntax enable` + stock colorscheme) | Regex-based, decent | Zero — works immediately, no internet |
| **lazy.nvim + nvim-treesitter + colorscheme plugin (chosen)** | Grammar-based, much more accurate | Needs git/internet on first launch |

Chosen: **lazy.nvim + treesitter + tokyonight**.

---

## 3. Plugin manager: lazy.nvim

[`lazy.nvim`](https://github.com/folke/lazy.nvim) is the plugin manager. It self-bootstraps: `init.lua` checks if `~/.local/share/nvim/lazy/lazy.nvim` exists, and if not, clones it automatically the first time Neovim runs. No manual install step needed.

---

## 4. nvim-treesitter: branch decision and the version wall

`nvim-treesitter` currently ships two incompatible branches:

- **`main`** (the repo's default/HEAD branch) — a full rewrite, requires **Neovim ≥ 0.12**. Old API (`require("nvim-treesitter.configs").setup{...}`) does not exist here.
- **`master`** — the legacy branch, compatible with Neovim 0.11, using the old `configs.setup{ ensure_installed = {...}, highlight = { enable = true } }` API.

**Decision: use `main`.**

This is where the setup hit its main obstacle. The installed Neovim was **0.11.6 (stable)**, but `main`'s code calls `vim.list.unique(...)` — an API that doesn't exist before 0.12. Running it produced:

```
attempt to index field 'list' (a nil value)
lua/nvim-treesitter/config.lua:171: in function 'norm_languages'
```

This confirmed the incompatibility wasn't a config error — `main` genuinely cannot run on 0.11.

**Fix: upgrade Neovim to nightly (0.12-dev)** rather than fall back to `master`, since the goal was to use `main`.

---

## 5. Installing Neovim nightly (no sudo, no apt/PPA changes)

Instead of adding the `neovim-ppa/unstable` PPA (a system-wide, harder-to-reverse change), the nightly **tarball** was downloaded straight from GitHub releases into a self-contained user directory:

```bash
mkdir -p ~/.local/nvim-nightly
cd ~/.local/nvim-nightly
curl -L -o nvim-linux-x86_64.tar.gz \
  https://github.com/neovim/neovim/releases/download/nightly/nvim-linux-x86_64.tar.gz
tar xzf nvim-linux-x86_64.tar.gz --strip-components=1
rm nvim-linux-x86_64.tar.gz
```

Result: `~/.local/nvim-nightly/bin/nvim` → `NVIM v0.13.0-dev-...` (satisfies the ≥0.12 requirement).

Added to `~/.bashrc` so this nightly build takes priority over the apt-installed `/usr/bin/nvim`:

```bash
export PATH="$HOME/.local/nvim-nightly/bin:$PATH"
```

The old `/usr/bin/nvim` (stable, apt-managed) was left untouched — this is purely additive and reversible by removing the PATH line.

---

## 6. Second dependency: `tree-sitter-cli`

Once on nightly, `:Lazy sync` progressed further but failed compiling parsers:

```
error: Error during "tree-sitter build": ENOENT: no such file or directory (cmd): 'tree-sitter'
```

`nvim-treesitter` (main branch) shells out to the real `tree-sitter` CLI (not the neovim binary) to compile parser grammars, and it wasn't installed. A C compiler (`gcc`/`cc`) was already present, so only the CLI was missing.

Installed via apt (requires sudo — run interactively by the user, not by the assistant, since it needs a password prompt):

```bash
sudo apt-get install -y tree-sitter-cli
```

This resolved the parser compilation step.

---

## 7. Final `init.lua`

Location: `~/.config/nvim/init.lua`

```lua
-- Basic options
vim.opt.number = true
vim.opt.termguicolors = true

-- Python (PEP8-style) indentation
vim.api.nvim_create_autocmd("FileType", {
  pattern = "python",
  callback = function()
    vim.opt_local.tabstop = 4
    vim.opt_local.shiftwidth = 4
    vim.opt_local.expandtab = true
    vim.opt_local.colorcolumn = "79"
  end,
})

-- Bootstrap lazy.nvim (plugin manager)
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  local lazyrepo = "https://github.com/folke/lazy.nvim.git"
  local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
  if vim.v.shell_error ~= 0 then
    vim.api.nvim_echo({
      { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
      { out, "WarningMsg" },
      { "\nPress any key to exit..." },
    }, true, {})
    vim.fn.getchar()
    os.exit(1)
  end
end
vim.opt.rtp:prepend(lazypath)

-- Plugins
require("lazy").setup({
  {
    "nvim-treesitter/nvim-treesitter",
    branch = "main",
    build = ":TSUpdate",
    config = function()
      require("nvim-treesitter").setup()
      require("nvim-treesitter").install({ "python", "lua", "vim", "vimdoc" }):wait(300000)
      vim.api.nvim_create_autocmd("FileType", {
        pattern = { "python", "lua", "vim" },
        callback = function() vim.treesitter.start() end,
      })
    end,
  },
  {
    "folke/tokyonight.nvim",
    priority = 1000,
    config = function()
      vim.cmd.colorscheme("tokyonight")
    end,
  },
})
```

Key points about the `main`-branch API (different from the old `master` API):
- `require("nvim-treesitter").setup()` — no `ensure_installed`/`highlight.enable` options anymore.
- `require("nvim-treesitter").install({...})` — installs parsers explicitly; `:wait(300000)` makes it synchronous (5 min cap) so it finishes before Neovim continues.
- Highlighting is **not automatic** — it must be turned on per filetype by calling `vim.treesitter.start()` in a `FileType` autocommand.

---

## 8. Verification method

Because this was scripted (no interactive terminal in this session), verification was done headlessly:

1. `nvim --headless '+Lazy! sync' +qa` — confirmed lazy.nvim cloned, parsers for `python`/`lua`/`vim`/`vimdoc` compiled and installed with no errors.
2. A test `.py` file with a decorator, typed function signature, docstring, f-string, comment, loop, and class was parsed directly via the Lua API:
   ```lua
   local parser = vim.treesitter.get_parser(bufnr, "python")
   local root = parser:parse()[1]:root()
   local query = vim.treesitter.query.get("python", "highlights")
   for id, node in query:iter_captures(root, bufnr, 0, -1) do ... end
   ```
   This returned **101 capture matches** across 30+ distinct highlight groups — `@keyword.function` (`def`), `@keyword.repeat` (`for`), `@keyword.return`, `@keyword.type` (`class`), `@string` / `@string.documentation`, `@comment`, `@function.builtin` (`print`, `range`), `@variable.parameter`, `@variable.builtin` (`self`), `@type.builtin` (`str`, `int`), etc.
3. **Caveat found along the way:** in pure headless mode, `vim.treesitter.highlighter.active[bufnr]` reports `true` but the actual extmarks stay at 0, and `vim.treesitter.get_captures_at_pos` returns nothing. This is *not* a config bug — Neovim's treesitter highlighter is a decoration provider that only computes highlights during a real screen redraw, and headless mode has no UI/redraw cycle. Querying the parser and highlight query directly (step 2 above) bypasses that and is the reliable way to confirm correctness without a real terminal.

Conclusion: highlighting is correctly configured and will render in color under normal interactive use (`nvim somefile.py` in a real terminal).

---

## 9. Result — file/directory reference

| Path | Purpose |
|---|---|
| `~/.config/nvim/init.lua` | Main Neovim config |
| `~/.local/nvim-nightly/bin/nvim` | Nightly Neovim binary (0.13.0-dev, satisfies treesitter `main`'s ≥0.12 requirement) |
| `~/.bashrc` | Has `PATH` line prepending nightly nvim ahead of the apt-installed stable one |
| `~/.local/share/nvim/lazy/` | Cloned plugins (`lazy.nvim`, `nvim-treesitter`, `tokyonight.nvim`) |
| `~/.local/share/nvim/site/parser/*.so` | Compiled treesitter parsers (python, lua, vim, vimdoc) |
| `~/.local/share/nvim/site/queries/python/highlights.scm` | Highlight query rules for Python |
| `/usr/bin/nvim` | Original stable apt-installed Neovim — untouched, still available if the `PATH` line is removed |
| `/usr/bin/tree-sitter` | `tree-sitter-cli` (apt), required to compile parser grammars |
| `~/.config/nvim/.luarc.json` | Pins `lua_ls`'s project root to `~/.config/nvim` (see §17) |
| `~/.local/share/nvim/mason/` | Mason's install root — `packages/`, `bin/` (symlinks), `registries/` |
| `~/.local/share/nvim/mason/bin/lua-language-server` | Installed Lua LSP server (works out of the box, no extra deps) |
| `~/.local/share/nvim/lazy/telescope.nvim`, `plenary.nvim`, `telescope-fzf-native.nvim` | Fuzzy finder + dependencies |
| `~/.local/share/nvim/lazy/mason.nvim`, `mason-lspconfig.nvim`, `nvim-lspconfig` | LSP installer + client config |
| `~/.local/share/nvim/lazy/nvim-cmp`, `LuaSnip`, `cmp-nvim-lsp`, `cmp-buffer`, `cmp-path`, `cmp_luasnip` | Autocompletion engine + sources |

---

## 10. Maintenance notes

- **Update plugins:** `:Lazy sync` inside Neovim.
- **Update/add parsers:** `:TSUpdate` or add a language to the `install({...})` list in `init.lua`.
- **Switch back to stable Neovim:** remove the `PATH` line from `~/.bashrc` — nothing else needs to change, since `/usr/bin/nvim` was never modified. (Note: this would break the `main`-branch treesitter config again, since stable is still 0.11.x pending a real 0.12 release — at that point pin `nvim-treesitter` to `master` instead, or wait for stable 0.12.)
- **Add more languages:** append to the `install({...})` table and the `FileType` autocmd `pattern` list in the treesitter plugin's `config` function.
- **Install an LSP server manually:** `:MasonInstall <package-name>` (Mason's package name, e.g. `lua-language-server`, `pyright` — not always the same as the lspconfig server name used in `vim.lsp.enable`, e.g. `lua_ls`). `:LspInstall` prompts interactively instead.
- **Add another LSP server:** `vim.lsp.config("<server>", {...})` + add it to the `vim.lsp.enable({...})` list and the `ensure_installed` table, both in the `nvim-lspconfig`/`mason-lspconfig` plugin specs in `init.lua`.

---

## 11. Recurrence — same crash seen again on a later launch

The exact `config.lua:171` / `vim.list` error from §4 showed up again on a separate occasion opening Neovim.

**Diagnosis:**
1. Re-read `~/.config/nvim/init.lua:34-47` — confirmed the plugin spec still pins `branch = "main"`, unchanged from §7.
2. Re-read `nvim-treesitter`'s `lua/nvim-treesitter/config.lua:171` in the installed plugin — still calling `vim.list.unique(languages)`.
3. Checked `nvim --version` **via a non-interactive shell** (`wsl.exe -e nvim --version`) — reported **0.11.6**, and `vim.list` was `nil` in that shell. This looked like the nightly install from §5 had gone missing or the PATH change hadn't survived.
4. Traced the exact commit that made `vim.list` mandatory instead of optional:
   ```
   git log -p --follow -S "vim.list.unique" -- lua/nvim-treesitter/config.lua
   ```
   Found `37bcfdc6 refactor(config): prefer vim.list.unique for normalization` (Aug 2025) originally added it **with a fallback**:
   ```lua
   -- TODO(clason): remove Nvim 0.11 compat
   if vim.list then
     return vim.list.unique(languages)
   else
     table.sort(languages)
     return vim.fn.uniq(languages)
   end
   ```
   Then a later commit, `c82bf96f feat!: drop support for Nvim 0.11`, deleted that fallback — `main` now hard-requires Neovim ≥ 0.12/nightly, unconditionally.
5. Checked `~/.bashrc` and found the nightly install *was* still there (`~/.local/nvim-nightly/bin`, added to `PATH` at line 128) and still worked — `wsl.exe -e bash -ic 'which nvim; nvim --version'` resolved to the nightly build (`v0.13.0-dev-1009+g1741da8412`), with `vim.list` present and populated.

**Root cause of the false alarm:** `.bashrc` only runs its PATH-modifying logic for *interactive* shells (the `case $- in *i*) ;; *) return;; esac` guard near the top). The first version-check command used a non-interactive `wsl.exe -e nvim ...` invocation, which skipped `.bashrc` entirely and silently fell back to the apt-installed `/usr/bin/nvim` (0.11.6). This made it look like the nightly install had regressed, when it was actually just not being reached by that particular check.

**Confirmed fix (no config or install changes needed):** in a real interactive shell, `nvim` resolves to the nightly build, `vim.list` exists, and both a headless plugin-load test and a headless open of a real `.py` file completed with no errors. The original §5 install and §7 `init.lua` are still correct as documented — opening a **new terminal** (so `.bashrc` re-sources cleanly) resolves the crash.

**Side effect noticed while diagnosing:** a redundant duplicate nightly build was accidentally downloaded to `~/.local/opt/nvim-nightly` while investigating (before the existing `~/.local/nvim-nightly` install was found). It was removed — the canonical nightly install remains only at `~/.local/nvim-nightly`, matching §5/§9.

**Takeaway for future troubleshooting:** always verify Neovim's resolved version/PATH from an **interactive** shell (`wsl.exe -e bash -ic '...'` or a real terminal), not a bare non-interactive one — `.bashrc`'s PATH changes won't apply otherwise, producing a misleading "nightly install disappeared" symptom.

---

## 12. Adding Telescope (fuzzy finder)

Added as a new plugin spec in `init.lua`:

```lua
{
  "nvim-telescope/telescope.nvim",
  branch = "0.1.x",
  dependencies = {
    "nvim-lua/plenary.nvim",
    { "nvim-telescope/telescope-fzf-native.nvim", build = "make" },
  },
  config = function()
    local telescope = require("telescope")
    telescope.setup()
    pcall(telescope.load_extension, "fzf")

    local builtin = require("telescope.builtin")
    vim.keymap.set("n", "<leader>ff", builtin.find_files, { desc = "Find files" })
    vim.keymap.set("n", "<leader>fg", builtin.live_grep, { desc = "Live grep" })
    vim.keymap.set("n", "<leader>fb", builtin.buffers, { desc = "List buffers" })
    vim.keymap.set("n", "<leader>fh", builtin.help_tags, { desc = "Help tags" })
  end,
},
```

`telescope-fzf-native.nvim` needed `make`/`gcc` to compile its native sorter — both were already present (same toolchain treesitter's parser compilation relies on), so no new system dependency here.

Since no keymap `leader` had been set anywhere in `init.lua`, `<leader>` defaulted to `\`. Set explicitly near the top of `init.lua` instead:

```lua
vim.g.mapleader = " "
vim.g.maplocalleader = " "
```

No blockers — cloned and worked on the first `Lazy sync`.

---

## 13. Adding LSP: the `require('lspconfig').setup{}` API is now hard-deprecated on nightly

Initial attempt used the classic pattern:

```lua
local lspconfig = require("lspconfig")
lspconfig.lua_ls.setup({ ... })
lspconfig.pyright.setup({ ... })
```

On the nightly build from §5 (v0.13.0-dev), this **errors** (not just warns):

```
The `require('lspconfig')` "framework" is deprecated, use vim.lsp.config (see :help lspconfig-nvim-0.11) instead.
Feature will be removed in nvim-lspconfig v3.0.0
```

nvim-lspconfig has moved to being a pure data provider (`lsp/*.lua` default configs) consumed by Neovim's own native LSP API, introduced in 0.11. The nightly build enforces this as a hard error, not a soft warning as the message text implies. **Fix — use the native API instead:**

```lua
local capabilities = require("cmp_nvim_lsp").default_capabilities()

vim.lsp.config("lua_ls", {
  capabilities = capabilities,
  settings = { Lua = { diagnostics = { globals = { "vim" } } } },
})

vim.lsp.config("pyright", {
  capabilities = capabilities,
})

vim.lsp.enable({ "lua_ls", "pyright" })
```

Buffer-local LSP keymaps are attached generically via an autocmd, so they apply no matter which server attaches to a given buffer:

```lua
vim.api.nvim_create_autocmd("LspAttach", {
  callback = function(args)
    local opts = { buffer = args.buf }
    vim.keymap.set("n", "gd", vim.lsp.buf.definition, opts)
    vim.keymap.set("n", "gD", vim.lsp.buf.declaration, opts)
    vim.keymap.set("n", "gr", vim.lsp.buf.references, opts)
    vim.keymap.set("n", "K", vim.lsp.buf.hover, opts)
    vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, opts)
    vim.keymap.set("n", "<leader>ca", vim.lsp.buf.code_action, opts)
    vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, opts)
    vim.keymap.set("n", "]d", vim.diagnostic.goto_next, opts)
    vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, opts)
  end,
})
```

Server installation is handled by `mason.nvim` + `mason-lspconfig.nvim`:

```lua
{ "williamboman/mason.nvim", config = function() require("mason").setup() end },
{
  "williamboman/mason-lspconfig.nvim",
  dependencies = { "williamboman/mason.nvim" },
  config = function()
    require("mason-lspconfig").setup({ ensure_installed = { "lua_ls", "pyright" } })
  end,
},
```

---

## 14. Autocompletion: `nvim-cmp`

Added alongside LSP so the servers are actually useful while typing, not just for hover/diagnostics:

```lua
{
  "hrsh7th/nvim-cmp",
  dependencies = {
    "hrsh7th/cmp-nvim-lsp", "hrsh7th/cmp-buffer", "hrsh7th/cmp-path",
    "L3MON4D3/LuaSnip", "saadparwaiz1/cmp_luasnip",
  },
  config = function()
    local cmp = require("cmp")
    local luasnip = require("luasnip")
    cmp.setup({
      snippet = { expand = function(args) luasnip.lsp_expand(args.body) end },
      mapping = cmp.mapping.preset.insert({
        ["<C-Space>"] = cmp.mapping.complete(),
        ["<CR>"] = cmp.mapping.confirm({ select = true }),
        ["<Tab>"] = cmp.mapping(function(fallback)
          if cmp.visible() then cmp.select_next_item()
          elseif luasnip.expand_or_jumpable() then luasnip.expand_or_jump()
          else fallback() end
        end, { "i", "s" }),
        ["<S-Tab>"] = cmp.mapping(function(fallback)
          if cmp.visible() then cmp.select_prev_item()
          elseif luasnip.jumpable(-1) then luasnip.jump(-1)
          else fallback() end
        end, { "i", "s" }),
      }),
      sources = cmp.config.sources(
        { { name = "nvim_lsp" }, { name = "luasnip" } },
        { { name = "buffer" }, { name = "path" } }
      ),
    })
  end,
},
```

`cmp-nvim-lsp`'s `default_capabilities()` is what gets passed into `vim.lsp.config(...)` in §13 — it tells the LSP servers that the client supports completion, so they return richer completion data than Neovim's bare defaults.

---

## 15. Verification quirk: `mason-lspconfig`'s `ensure_installed` silently no-ops in headless mode

Since this session also has no interactive terminal, verification tried the same headless pattern as §8 (`nvim --headless -c 'lua vim.wait(45000)' -c 'qa'`) and waited for Mason to auto-install `lua_ls`/`pyright` per `ensure_installed`. Nothing appeared in `~/.local/share/nvim/mason/packages` no matter how long the wait.

Root cause, found in `mason-lspconfig.nvim`'s source (`lua/mason-lspconfig/init.lua`):

```lua
if not platform.is_headless and #settings.current.ensure_installed > 0 then
    require "mason-lspconfig.features.ensure_installed"()
end
```

This is deliberate: `ensure_installed` is explicitly skipped when Neovim is running `--headless`, to avoid unattended installs during scripted/CI usage. **Not a config bug** — on a normal interactive launch (just running `nvim` in a real terminal), it fires automatically.

For headless verification, servers were installed explicitly instead: `:MasonInstall lua-language-server` (Mason's package name — note this differs from the lspconfig/`vim.lsp.enable` server name `lua_ls`; `mason-lspconfig` is what translates between the two, e.g. `:MasonInstall lua_ls` on its own fails with `"lua_ls" is not a valid package`).

`lua_ls` installed cleanly (GitHub release tarball, no extra system deps) and was confirmed attaching to `~/.config/nvim/init.lua`:

```lua
vim.tbl_map(function(c) return c.name end, vim.lsp.get_clients())
-- { "lua_ls" }
```

---

## 16. `pyright` install: broken by a Windows npm mixed into a WSL PATH

Python LSP needs `pyright`, which Mason installs via `npm`. Checking the toolchain first:

| Tool | Found | Note |
|---|---|---|
| `node` | `/usr/bin/node` v22.22.1 | Native WSL install (apt `nodejs` package) |
| `npm` | `/mnt/d/NodeJS/npm` | **Windows** npm, reached via a `/mnt/d/...` PATH entry — no WSL-native `npm` package is installed |
| `pip3` / `pipx` | not found | `python3 -m pip` → `No module named pip`; `python3 -m venv` also fails (`ensurepip is not available`, needs `apt install python3.14-venv`) |

Both install paths for Python LSP servers were blocked: `pyright` needs a working npm, `pylsp` (the pip-based alternative) needs `python3-venv`/pip. **Decision: fix npm, use `pyright`** (more actively maintained, better type checking than `pylsp`) rather than fix the pip toolchain for a fallback server.

Running `:MasonInstall pyright` with the broken (Windows) npm on PATH did not fail outright — it actually completed (`added 1 package, and audited 2 packages`, `found 0 vulnerabilities`), but with a wall of warnings during unpacking:

```
npm warn tar TAR_ENTRY_ERROR ENOENT: no such file or directory, lstat '\\wsl.localhost\Ubuntu\home\filtz21\.local\share\nvim\mason\staging\pyright\node_modules\pyright\dist'
```

The install *looked* successful (`dist/` was present, correctly sized files, `mason/bin/pyright` symlink created), but running the binary revealed it was actually broken:

```
node:internal/modules/cjs/loader:1503
Error: Cannot find module '\\wsl.localhost\Ubuntu\home\filtz21\.local\share\nvim\mason\pyright\index.js'
...
Node.js v24.16.0
```

Two tells that this is the Windows/WSL npm mismatch, not a corrupted download:
1. The error path is a Windows UNC path (`\\wsl.localhost\...`), not a Linux path — the npm-generated wrapper script was written in a Windows-native style.
2. `Node.js v24.16.0` — a **different** Node version than the WSL-native one (`v22.22.1`) that ran the actual `nvim`/Mason process. The Windows npm shells out to a Windows-installed Node, not the Linux one, when generating the executable shim.

**This package was uninstalled** (`:MasonUninstall pyright`) rather than left in place — a package that exists on disk but silently fails to launch is worse than no package, since it would make `vim.lsp.enable("pyright")` fail with a confusing runtime error instead of a clear "not installed" state.

**Required fix (not run by the assistant — needs an interactive `sudo` password prompt):**

```bash
sudo apt-get install -y npm
```

`/usr/bin` already precedes every `/mnt/...` entry in `$PATH`, so once a native `npm` package exists there, it will automatically take priority over the Windows one — no `PATH` edit needed, unlike the nightly-Neovim fix in §5. After that, either run `:MasonInstall pyright` again or just open `nvim` normally once — `ensure_installed` (see §15) will pick it up automatically on a real interactive launch.

---

## 17. `lua_ls` workspace warning → `.luarc.json`

With `lua_ls` attached (§15) and editing `init.lua` directly, it reported:

```
LSP[lua_ls] Your workspace is set to `/home/filtz21`. Lua language server refused to load this directory.
```

Cause: `vim.lsp.config`'s default root-dir detection for `lua_ls` climbs up from the current file looking for a project marker (`.luarc.json`, `.git`, etc.); finding none between `~/.config/nvim/init.lua` and `$HOME`, it fell back to `$HOME` itself — which `lua_ls` then refuses to index (far too broad, would try to scan the entire home directory).

Fix: added a minimal `~/.config/nvim/.luarc.json` so the root-marker search stops there instead:

```json
{
  "runtime.version": "LuaJIT",
  "diagnostics.globals": ["vim"],
  "workspace.checkThirdParty": false
}
```

Verified after adding it — `root_dir` now correctly resolves to `~/.config/nvim` and the warning is gone:

```lua
vim.tbl_map(function(c) return {c.name, c.config.root_dir} end, vim.lsp.get_clients())
-- { { "lua_ls", "/home/filtz21/.config/nvim" } }
```

---

## 18. Keymap reference (Telescope + LSP)

| Keys | Action |
|---|---|
| `<space>ff` | Telescope: find files |
| `<space>fg` | Telescope: live grep |
| `<space>fb` | Telescope: list buffers |
| `<space>fh` | Telescope: search help tags |
| `gd` | LSP: go to definition |
| `gD` | LSP: go to declaration |
| `gr` | LSP: find references |
| `K` | LSP: hover docs |
| `<space>rn` | LSP: rename symbol |
| `<space>ca` | LSP: code action |
| `[d` / `]d` | LSP: previous/next diagnostic |
| `<space>e` | LSP: show diagnostic detail for current line |
| `<Tab>` / `<S-Tab>` | Completion menu: next/previous item (insert mode) |
| `<CR>` | Completion menu: confirm selection (insert mode) |
| `<C-Space>` | Completion menu: force open (insert mode) |

(`<leader>` is `<space>`, set explicitly in §12 — previously unset, defaulting to `\`.)
