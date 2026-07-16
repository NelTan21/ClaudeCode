# git_commands.sh
# Reference sheet for common Git commands (Ubuntu)


# ===================================================================
# Install & Setup
# ===================================================================
sudo apt update
sudo apt install software-properties-common  # enables the add-apt-repository command
sudo add-apt-repository ppa:git-core/ppa
sudo apt update
sudo apt install git
sudo apt-get install language-pack-en # This allows git to display messages in English (if your system is set to a different language)
        export LANG=en_US.UTF-8 # This sets the system language to English (US) for Git commands
        export LC_ALL=en_US.UTF-8 # This sets the system locale to English (US) for Git commands
                # If above command fails
                sudo locale-gen en_US.UTF-8
                sudo update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 LANGUAGE=en
                locale -a | grep -i en_US
                /etc/default/locale # This file contains the system-wide locale settings, including the LANGUAGE variable. You can edit this file to set the default language for all users on the system.
                        filtz21@Panda2:/etc/default$ cat locale
                                LANG=en_US.UTF-8
                                LANGUAGE=en
                                LC_ALL=en_US.UTF-8
        export LANGUAGE=en # This sets the system language to English for Git commands
curl -sS https://webi.sh/gh | sh # Install GitHub

# ===================================================================
# Help & Manual
# ===================================================================
git help git   # open the full git manual page

# Manual navigation shortcuts (while inside `git help git` / `man git`):
#   q          quit the manual
#   j          one line down
#   k          one line up
#   d          half page down
#   u          half page up
#   /<term>    search for "term"
#   n          jump to next search match
#   N          jump to previous search match


# ===================================================================
# Configuration  (Ancillary Command)
# ===================================================================
git rev-parse --show-toplevel                   # Show the root Repo for your Git Repository
git config --global user.name "Your Name"                # set the name attached to your commits
git config --global user.email "your.email@example.com"  # set the email attached to your commits

# Newer subcommand syntax (Git 2.46+) -- does the same thing, clearer verbs:
git config set --global user.name "NelTan21"
git config set --global user.email "nel.tan21@gmail.com"
git config set --global init.defaultBranch master   # set the default branch name for new repos (e.g. master or main)

git config get user.name   # -> NelTan21               (read back a single config value)
cat ~/.gitconfig           # view the full config file directly, e.g.:
#   [user]
#           name = NelTan21
#           email = nel.tan21@gmail.com
#   [init]
#           defaultBranch = master

# Local (per-repository) config -- overrides --global, only applies inside the current repo:
git config --local user.email "different.email@example.com"  # e.g. use a work email just for this repo
git config list --local     # list only the config values scoped to THIS repository (Git 2.46+ syntax; old form: git config --list --local)
cat .git/config              # view the local config file directly -- lives inside .git/, not your home directory

# Deleting a config entry:
git config --unset user.email                 # remove a key (whichever scope git checks by default)
git config --local --unset user.email           # remove specifically from .git/config (this repo only)
git config --global --unset user.email            # remove specifically from ~/.gitconfig
git config unset --local user.email                 # newer subcommand syntax, same effect
git config unset --all user.email                       # removes all related key.value pairs
git config --unset-all <key>                           # remove EVERY matching instance of a key that allows duplicates
git config --remove-section alias                         # remove an entire section (e.g. all of [alias]), not just one key
git config --edit --local                                   # open .git/config directly in your default editor to edit/delete by hand
git config set pull.rebase false                              # git will merge on a pull
git config set --global pull.rebase true                        # git will rebase on pull

# ===================================================================
# Starting a Repository  (Porcelain)
# ===================================================================
git init            # create an empty Git repository in the current directory (or reinitialize an existing one)
git clone <repo>     # copy an existing repository (local path or URL) into a new directory


# ===================================================================
# Local Workflow -- Staging & Committing  (Porcelain)
# ===================================================================
git status                  # show the working tree status: staged, unstaged, and untracked changes
git add <file>               # add file contents to the index (staging area)
git diff                      # show unstaged changes -- working tree vs. the index
git diff --staged              # show staged changes -- index vs. the last commit
git commit -m "message"          # record staged changes as a new commit
git log                            # show commit history
git log --decoration=short/full/no  # shows log in either short, full, or no branch reference
git log --oneline                   # shows log in compacted one liner prints
git --no-pager log -n 10            # show the last 10 commits without paging
git log --oneline --graph --all      # provides a line graph pointing to branch flows(splits and merges)
git rm <file>                        # remove a file from the working tree and the index
git mv <old> <new>                     # move or rename a file, directory, or symlink
git reset <file>                         # unstage a file (remove from index, keep the changes in your working tree)
git reset --hard COMMITHASH                 # move HEAD to <commit> and discard all changes since (destructive) DELETED FOR GOOD!
git reset --soft COMMITHASH                   # Go back to a previous commithash, commited becomes staged, uncommited becomes staged/unstaged.


# ===================================================================
# Branching & Merging  (Porcelain)
# ===================================================================
git branch                # list local branches (git branch <name> creates one)
git branch <new>           # create a new branch
git switch <branch>         # switch to an existing branch
git switch -c <branch>        # create a new branch and switch to it in one step
git checkout <branch>           # older, overloaded equivalent -- switches branches OR restores files, depending on args
git restore <file>                # discard unstaged changes to a file (modern replacement for `checkout -- <file>`)
git merge <branch>                  # merge <branch> into the current branch
git branch -m <oldname> <newname>     # rename an existing branch
directory -> .git/refs/heads            # contains a file for each branch which holds the commit hashes pointed to it
git switch -c update_dune COMMITHASH     # creates a new branch where its tip starts from the commit hash.
git branch -vv

# ===================================================================
# Working with Remotes  (remote = Ancillary; fetch/pull/push = Porcelain)
# ===================================================================
git remote -v        # list configured remote repositories and their URLs
git ls-remote         # list remote repo addresses
git fetch              # download objects and refs from a remote, without merging
git pull                 # fetch AND merge (or rebase) from a remote branch into the current branch
git pull <remote>/<branch> # fetch from specified remote branch into specified local branch
git push                   # upload local commits to a remote branch
git push <remote>/<branch>  # upload specified local branch commits to specified remote branch
git remote add <name> <url>     # creates and names a remote connection to an existing repo, target URL or relative path
git remote remove <name>        # remove a remote repo
git remote show origin       # detailed info on the "origin" remote -- tracked branches, ahead/behind status, etc.
git remote get-url origin      # print just the URL configured for "origin"
git remote add origin <url>      # "origin" is just a convention -- the default name Git suggests for your primary remote
git remote set-url origin <url>    # change the URL "origin" points to (e.g. after a repo moves, or switching http -> ssh)
git remote rename origin upstream    # rename a remote (e.g. common when adding a fork's real source as a second remote)
git remote remove origin               # disconnect "origin" -- only removes the local reference, does NOT delete the remote repo itself
git log <remote_repo>/<branch_name> --oneline # returns the commit logs from the branch into your remote repo's log
# ===================================================================
# Stashing & Tags  (Porcelain)
# ===================================================================
git stash                     # temporarily shelve uncommitted changes so you can switch context
git stash pop                   # reapply the most recently stashed changes and remove them from the stash list
git tag <tagname>                 # create a lightweight tag pointing at the current commit
git tag -a <tagname> -m "message"   # create an annotated tag (recommended -- stores author, date, and message)


# ===================================================================
# Plumbing (Low-Level) Commands -- Git's internal building blocks, rarely used directly
# ===================================================================
git apply <patch>          # apply a patch to files and/or the index
git apply --check <patch>    # verify a patch would apply cleanly, without actually applying it
git commit-tree <tree>          # create a new commit object directly, without touching the index
git hash-object <file>             # compute the SHA-1 object ID of a file (add -w to also store it as a blob)
git cat-file -p <hash>                # pretty-print the contents of a Git object (commit, tree, or blob) given its SHA
        # filtz21@Panda2:~/Git/webflyx$ git cat-file -p 9d8b9fefa44ee9da78a8f22cffd63614cb922904 >> /tmp/catfileout.txt
        # filtz21@Panda2:~/Git/webflyx$ cat /tmp/catfileout.txt
                # tree 5b21d4f16a4b07a6cde5a3242187f6a5a68b060f
                # author NelTan21 <nel.tan21@gmail.com> 1783859552 +0800
                # committer NelTan21 <nel.tan21@gmail.com> 1783859552 +080
git cat-file -t <hash>                  # show the TYPE of an object (commit, tree, blob, or tag) instead of its contents
git cat-file 
xxd /path/object/file # The raw bytes contents of the version for that specific code branch
        # sometimes have quirks to have an 8bit column padding(00000010) instead of 7(0000010)
find .git/objects -type f   # list every object currently stored in the repo (files only -- skips the hash-prefix directories)


# ===================================================================
# gitignore: 
# ===================================================================
        # A problem arises when we want to put files in our project's directory, 
        # but we don't want to track them with Git. 
        # A .gitignore file solves this. For example, if you work with Python, 
        # you probably want to ignore automatically generated files like .pyc and __pycache__. 
        # If you are building a server, you probably want to ignore .env files that might hold private keys. 
        # If you (I'm sorry) work with JavaScript, you might want to ignore the node_modules directory.
touch .gitignore        # creates a gitignore file
cat .gitignore          # add files to ignore
        #  a .gitignore file can only affect its own directory and everything below it:
        node_modules/ -> Directory
        /config.local.json -> current location file
        *.txt -> wildcard to ignore files with .txt suffix
        !/important.txt -> don't ignore file
                # Order matters, if wildcard and negation were reversed then negation would be overridden

# WHAT TO IGNORE
        # Ignore things that can be generated (e.g. compiled code, minified files, etc.)
        # Ignore dependencies (e.g. node_modules, venv, packages, etc.)
        # Ignore things that are personal or specific to how you like to work (e.g. editor settings)
        # Ignore things that are sensitive or dangerous (e.g. .env files, passwords, API keys, etc.)                

# ===================================================================
# Notes: 
# ===================================================================
Hash:
- SHA, Git uses a cryptographic hash function called SHA-1 to generate commit hashes. 
- We won't go into the details of how SHA-1 works in this course.
- but it's important to know because you might also hear commit hashes referred to as "SHAs".

# What affects the hash of a commit?
The hash of a commit is affected by the following factors:
- The content of the files being committed
- The commit message
- The author and committer information (name and email)
- The timestamp of the commit
- The parent commit(s) (if any)
- The tree structure of the repository at the time of the commit

Git is made up of objects that are stored in the .git/objects directory.


#Git-specific aliases:
        # Git also has its own alias system, 
        # stored in ~/.gitconfig:
        # example: git config --global alias.co checkout
                # alias > function identifier
                # .variable > alias name
                # checkout > function name that is aliased
git config --global alias.co checkout 
git config --global alias.st status
git config --global alias.last "log -1 HEAD"


# Locations: respectively, each location encompasses the next
system: /etc/gitconfig, a file that configures Git for all users on the system
global: ~/.gitconfig, a file that configures Git for all projects of a user
local: .git/config, a file that configures Git for a specific project
worktree: .git/config.worktree, a file that configures Git for part of a project

# ===================================================================
# WSL Push Fix: HTTP/2 framing errors & MTU
# ===================================================================
# Root cause: git's HTTP/2 transport gets disrupted mid-push, often due to
# corporate network/proxy/antivirus interference, or WSL2's default MTU
# not matching the host's. Fix: force HTTP/1.1, raise the push buffer,
# and clamp the WSL interface MTU.

git config --global http.version HTTP/1.1
git config --global http.postBuffer 524288000

# Clamp eth0 MTU to 1400 on every WSL boot -- add to /etc/wsl.conf:
#   [boot]
#   systemd=true
#   command="ip link set dev eth0 mtu 1400"

# Verification:
ip link show eth0 | grep mtu             # confirm the interface picked up mtu 1400
git config --get http.version            # confirm HTTP/1.1 is set
git config --get http.postBuffer         # confirm postBuffer is set
git fetch origin && git diff main origin/main   # confirm local == remote after a push