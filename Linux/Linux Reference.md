REPL
Shells are often referred to as "REPLs." REPL stands for
Read
Eval (evaluate)
Print
Loop

Absolute vs. Relative Paths
Absolute path is the navigation to a specific destination from the root directory
Relative path is the navigation to a specific destination from your current directory 

Compiled vs. Interpreted
A compiled program is a program that has been converted from human-readable source code into machine code (binary). Machine code is a set of instructions that a computer can execute directly: your computer's CPU is hardware that's been designed to execute machine code.
Programming languages like Go, C, and Rust produce compiled programs.

An interpreted program is a program that is executed by another program. The program that executes the interpreted program is called an interpreter. The interpreter reads the source code of the interpreted program and executes it.
Programming languages like Python, Ruby, and JavaScript, are typically interpreted as they run, which means your computer needs to have the interpreter installed to run the program.
Another example is the .sh shell script files we talked about. Those are interpreted by the shell program.


#! = "sha-bang" = "shebang."


If you're using Ubuntu on WSL, you're probably running a Bash shell.
If you're using macOS, you're probably running a Zsh shell.
If you're running a raw Linux installation, I pray you already know what you're using.
To get hand-wavy about it, I want to explain the difference between the 3 shells you're likely to encounter:

sh: The Bourne shell. This is the original Unix shell and is POSIX-compliant. It's very basic and doesn't have many quality-of-life features.
bash: The Bourne Again shell. This is the most popular shell on Linux. It builds on sh, but also has a lot of extra features.
zsh: The Z shell. This is the most popular shell on macOS. Like bash, it does what sh can do, but also has a lot of extra features.


Why Do We Care About the PATH?
If it weren't for the PATH, you'd have to remember the filesystem path of every executable you wanted to run in your shell. Instead of just running ls, you'd have to run /bin/ls (or whatever the location of the ls executable is on your system). That's not very convenient.

The PATH variable is a list of directories that your shell will look into when you try to run a command. If you type ls, your shell will look in each directory listed in your PATH variable for an executable called ls. If it finds one, it will just run it. If it doesn't, it will give you an error like: "command not found."

Conventions
Whether or not a command takes flags, and what those flags are, is up to the developer of the command. That said, there are some common conventions:

Single-character flags are prefixed with a single dash (e.g. -a)
Multi-character flags are prefixed with two dashes (e.g. --help)
Sometimes the same flag can be used with a single dash or two dashes (e.g. -h or --help)

Unix Philosophy
The Unix Philosophy is a simple set of principles that have guided the development of Unix-like operating systems for decades. It can be summarized as:

Write programs that do one thing and do it well.
Write programs to work together.
Write programs to handle text streams, because that is a universal interface.


Terminal Alternatives
So far you've likely been working in the default terminal that came with your operating system, and that's fine. However, there are other options, and I want to highlight a couple of them just in case you want to check them out (but you don't have to).

Editor/IDE Built-in Terminals
Most text editors for developers have a built-in terminal.

For example, VS Code, Zed, and Cursor are popular text editors that also have a built-in terminal. While I do use Zed's terminal for most of my coding work, in this course, I do not recommend using a built-in terminal because we don't need the extra text editor features.

Ghostty
Ghostty is a very new terminal emulator that differentiates itself by being fast, feature-rich, and native. It's a great option if you love to customize, and want a modern, fast, and feature-rich terminal.

Alacritty
Alacritty is another popular terminal emulator that is known for its speed and extensibility. Before Ghostty, Alacritty was the go-to terminal for many developers who wanted a fast and customizable terminal.

Windows Terminal
Windows Terminal is the terminal emulator for Windows. Use the "cmd.exe" program settings to change the default terminal. Be sure to start WSL whenever you open a new terminal window.


apt (Advanced Package Tool) is Ubuntu/Debian's package manager - a command-line tool for installing, updating, and removing software on your system.
Repositories (repos) are servers that host packages (pre-compiled software plus metadata). Ubuntu maintains official repos, and there are third-party ones too.
Your system has a list of these repo URLs configured in /etc/apt/sources.list (and files in /etc/apt/sources.list.d/).


Symbolic Links
A symbolic link, usually called a symlink for short, is a special kind of file that points to another file or directory.
It's a lot like a shortcut in a GUI. The symlink has its own path, but when you use it, the operating system follows the link to the target.

Sudo
The sudo keyword lets you run a command as the root "superuser".


Let's break down each character. The first one just tells you whether you're looking at a file or a directory:

-: Regular file (e.g. -rwxrwxrwx)
d: Directory (e.g. drwxrwxrwx)
The next 9 characters are broken up into 3 sets of rwx and represent the permissions themselves for the "owner," "group," and "others," in order. Each group of 3 represents the permissions for reading, writing, and executing, in order. So, for example:

rwx: All permissions

rw-: Read and write, but not execute

r-x: Read and execute, but not write

The first 3 characters are "owner" permissions. The "owner" is usually just the user who created the file or directory, but it can be manually changed.

The next 3 characters are "group" permissions. Unix-like systems support groups of users, and each file or directory is assigned to exactly one owning group. Anyone who is not the owner and not a member of that group falls under "others." To be honest, unless you're a system administrator, you won't often worry about groups.

The last 3 characters are "others" permissions. This is everyone else.

In my experience, when you're doing programming work on your own local machine, you mostly just care about the "owner" permissions because that's usually you. Here are some full examples:

-rwxrwxrwx: A file where everyone can do everything
-rwxr-xr-x: A file where everyone can read and execute, but only the owner can write
drwxr-xr-x: A directory where everyone can read (ls the contents) and execute (cd into it), but only the owner can write (modify the contents)
drwx------: A directory where only the owner can read, write and execute