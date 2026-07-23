dd       cut the current line
3dd      cut 3 lines starting at the cursor
dj       cut current line + line below
dk       cut current line + line above
p        paste after the cursor / below the current line
P        paste before the cursor / above the current line
yy       copy the current line
3yy      copy 3 lines
V        enter visual line mode
j/k      extend selection down/up
d        cut the selection
y        copy the selection
p / P    paste after / before
u        undo
Ctrl+r   redo
:qa      quit all
:wq      write and quit
:w       write
:q!      quit without saving
Ctrl+v   enter visual block mode
Ctrl+c   copy selection in visual mode
Ctrl+x   cut selection in visual mode
Ctrl+v   paste selection in visual mode
:%s/\r$//g Remove trailing ^M from pasted windows lines

-- Movement --
w / b / e     jump to next / previous / end of word
0 / ^ / $     start of line / first non-blank / end of line
gg / G        top / bottom of file
{ / }         jump by paragraph/block
%             jump to matching ( { [
Ctrl+d/Ctrl+u half-page down/up
f<char>       jump to next occurrence of a character on the line
t<char>       jump to just before next occurrence of a character
;             repeat last f/t

-- Editing beyond dd/yy/p --
ci"           change inside quotes (works with ' ( [ { too)
di(           delete inside parens
da{           delete a block including the braces
yiw           yank inner word
yaw           yank a word (includes trailing whitespace/punctuation)
.             repeat last change
>> / <<       indent / outdent line
J             join current line with the next
~             toggle case of character under cursor

-- Search & replace --
/pattern      search forward, n/N repeat forward/backward
:%s/old/new/g replace all occurrences in file
:%s/old/new/gc replace all, confirm each one
*             search for word under cursor, forward
#             search for word under cursor, backward
g* / g#       same as */#, but partial match instead of whole-word
:noh          clear search highlighting (comes back on next search)

-- Macros --
qa ... q      record macro into register a
@a            replay macro a
5@a           replay macro a 5 more times
@@            repeat last macro

-- Buffers / windows / tabs --
:e <file>     open another file without leaving nvim
:ls           list open buffers
:b <number>   switch to buffer number
:bnext/:bprev cycle buffers
:sp / :vsp    split window horizontal / vertical
Ctrl+w h/j/k/l move between splits
:tabnew       new tab
gt            go to next tab
gT            go to previous tab
{n}gt         go directly to tab number n (e.g. 2gt jumps to tab 2)
:tabn/:tabp   next / previous tab (command form of gt/gT)
:tabc         close current tab
:tabo         close all tabs except the current one
:tabs         list all open tabs and their windows

-- Marks & jumps --
ma            set mark a
`a            jump to mark a
Ctrl+o/Ctrl+i back/forward through jump history

-- Telescope (fuzzy finder, leader = space) --
<space>ff     find files
<space>fg     live grep (search text across files)
<space>fb     list open buffers
<space>fh     search help tags

-- LSP (lua_ls, pyright) --
gd            go to definition
gD            go to declaration
gr            find references
K             hover docs
<space>rn     rename symbol
<space>ca     code action
[d / ]d       previous / next diagnostic
<space>e      show diagnostic detail for current line

-- Completion (nvim-cmp, insert mode) --
Tab / S-Tab   next / previous completion item
Enter         confirm selection
Ctrl+Space    force open completion menu

-- Class/method blocks (Python methods are separated by blank lines, so paragraph motions = method motions) --
vip           select inner paragraph (whole method body)
dap           delete a method block including its trailing blank line
>ip / <ip     indent / outdent a whole method at once

-- Folding (collapse classes you're not editing) --
zf<motion>    create a fold over that block (e.g. zfip)
za            toggle fold open/closed under cursor
zR / zM       open all folds / close all folds

-- Tweaking values fast (e.g. num_arrows, use_arrows(3)) --
Ctrl+a/Ctrl+x increment / decrement the number under the cursor

-- Misc navigation --
gf            open the file path under the cursor
`[ / `]       jump to start / end of last yanked or changed text
zz / zt / zb  center / scroll current line to top / bottom
gv            reselect last visual selection

-- OOP/inheritance workflow (uses LSP keymaps above) --
gd on super().__init__(...)   jump to the parent class's __init__
gr on a parent method         find every subclass call site (the "gateway method" pattern)
<space>fg                     grep across activity + test file without manual :e

-- More mobility: screen & file navigation --
H / M / L     jump to top / middle / bottom of the visible screen
Ctrl+f/Ctrl+b full page down / up
Ctrl+e/Ctrl+y scroll the view one line down / up without moving the cursor
W / B / E     jump by WORD (punctuation-inclusive) instead of word — skips over target.get_name() in one hop
gj / gk       move by display line instead of file line (useful on wrapped comment lines)
{number}G     jump straight to a line number (e.g. 33G)
Ctrl+^        toggle to the alternate file (e.g. flip between inheritance.py and inheritance_test.py)
gi            re-enter insert mode at the last place you were inserting

-- System clipboard setup (WSL) --
"+yip         yank inner paragraph into the SYSTEM clipboard (register +)
"+yy          yank current line into the system clipboard
"+y           (visual mode) yank selection into the system clipboard
"+p           paste from the system clipboard into nvim
-- plain yy/yip/p only fill nvim's internal register — other apps can't see it.
-- "+ routes through xclip to the shared/Windows clipboard instead.

Setup steps (one-time, only needed if the commands above don't work):
1. sudo apt install xclip           -- installs the clipboard bridge tool
2. echo $DISPLAY                    -- should print something like :0 (WSLg X server); if empty, clipboard bridging won't work
3. nvim --headless -c 'checkhealth provider' -c 'qa!'   -- confirms nvim found xclip (look for "Clipboard tool found: xclip")
-- no init.lua changes needed — nvim auto-detects xclip once it's installed and DISPLAY is set.

-- Visual block mode in VS Code's integrated terminal --
-- Ctrl+v and Ctrl+q are both intercepted by VS Code (paste / quick open)
-- before they reach nvim, so init.lua remaps block-visual mode instead:
<space>v      enter visual block mode (custom leader mapping, replaces Ctrl+v/Ctrl+q)

