echo "I use Linux btw" # prints text back out to you
echo $PATH | tr ':' '\n' | grep "something" # prints the PATH variable, replaces colons with newlines, and filters the output to show only lines containing "something"
expr 123456 + 7890 # evaluates a simple expression and prints the result
whoami # prints the username of the user you're currently logged in as.
name="Lane" # Creates a variable called name and assigns it the value "Lane"
echo Hello $name # Interpolating a Variable in a String
history # prints a list of commands that have been run in the current shell session               
clear or ctrl+L # clears the terminal window
pwd  # prints the current working directory
ls # lists the files and directories in the current working directory
ls -l # lists the files and directories in the current working directory in long format, showing additional details such as permissions, ownership, size, and modification date
ls -a # lists all files and directories in the current working directory, including hidden files (those starting with a dot)
ls -lh # lists the files and directories in the current working directory in long format with human-readable file sizes (e.g., KB, MB)
ls -R # lists the files and directories in the current working directory and all of its subdirectories recursively
ls -t # lists the files and directories in the current working directory sorted by modification time, with the most recently modified files first
ls -tr # lists the files and directories in the current working directory sorted by modification time, with the oldest modified files first
ls -X # lists the files and directories in the current working directory sorted by file extension
ls -1 # lists the files and directories in the current working directory in a single column format
ls -d */ # lists only the directories in the current working directory
ls -S # lists the files and directories in the current working directory sorted by file size, with the largest files first
ls -r # lists the files and directories in the current working directory in reverse order
ls dir1 dir2 | grep "search_term" # lists the files and directories in dir1 and dir2, and filters the output to show only those that contain "search_term"
cd # changes the current working directory to the specified directory
cat # prints the contents of a file to the terminal
head -n 10 file1.txt # prints the first 10 lines of file1.txt
tail -n 10 file1.txt # prints the last 10 lines of file1.txt
more # prints the contents of a file one page at a time
less # similar to more, but allows for backward navigation through the file
q # quits the more or less command
touch file1.txt # creates a new empty file called file1.txt
mkdir new_directory # creates a new directory called new_directory
mkdir -p new_directory/sub_directory # creates a new directory called sub_directory inside new_directory, creating any necessary parent directories
mkdir -v new_directory # creates a new directory called new_directory and prints a message indicating that the directory was created
mkdir -m 755 new_directory # creates a new directory called new_directory with permissions set to 755 (read, write, and execute for the owner; read and execute
mkdir -p new_directory/sub_directory && cd new_directory/sub_directory # creates a new directory called sub_directory inside new_directory and changes the current working directory to sub_directory
mkdir -p new_directory/sub_directory && touch new_directory/sub_directory/file1.txt # creates a new directory called sub_directory inside new_directory and creates a new empty file called file1.txt inside sub_directory
mkdir -p new_directory/sub_directory && echo "Hello World" > new_directory/sub_directory/file1.txt # creates a new directory called sub_directory inside new_directory and writes "Hello World" to a new file called file1.txt inside sub_directory
mkdir -p new_directory/sub_directory && echo "Hello World" > new_directory/sub_directory/file1.txt && cat new_directory/sub_directory/file1.txt # creates a new directory called sub_directory inside new_directory, writes "Hello World" to a new file called file1.txt inside sub_directory, and prints the contents of file1.txt to the terminal
mv file1.txt new_directory/ # moves file1.txt into new_directory
mv new_directory/file1.txt file2.txt # renames file1.txt to file2.txt within new_directory
mv new_directory/file2.txt new_directory/file3.txt # renames file2.txt to file3.txt within new_directory
cp file1.txt new_directory/ # copies file1.txt into new_directory
cp -R new_directory/ new_directory_copy/ # copies new_directory and all of its contents into a new directory called new_directory_copy
rm file1.txt # deletes file1.txt
rm -r new_directory/ # deletes new_directory and all of its contents
grep "search_term" file1.txt # searches for "search_term" in file1.txt and prints matching lines
grep "search_term" file1.txt file2.txt # searches for "search_term" in both file1.txt and file2.txt and prints matching lines
grep -r "search_term" /path/to/directory/ # searches for "search_term" in all files within the specified directory and its subdirectories
grep -i "search_term" file1.txt # searches for "search_term" in file1.txt, ignoring case
grep -v "search_term" file1.txt # prints all lines in file1.txt that do not contain "search_term"
grep -n "search_term" file1.txt # prints matching lines along with their line numbers
grep -c "search_term" file1.txt # counts the number of lines in file1.txt that contain "search_term"
grep -l "search_term" /path/to/directory/ # lists the names of files in the specified directory that contain "search_term"
grep -L "search_term" /path/to/directory/ # lists the names of files in the specified directory that do not contain "search_term"
grep -E "pattern1|pattern2" file1.txt # searches for lines that match either pattern1 or pattern2 in file1.txt
grep -A 3 "search_term" file1.txt # prints matching lines along with the 3 lines that follow them
grep -B 3 "search_term" file1.txt # prints matching lines along with the 3 lines that precede them
grep -C 3 "search_term" file1.txt # prints matching lines along with the 3 lines that precede and follow them
grep -o "search_term" file1.txt # prints only the matching parts of lines in file1.txt
grep -w "search_term" file1.txt # searches for whole word matches of "search_term" in file1.txt
grep -P "pattern" file1.txt # uses Perl-compatible regular expressions to search for "pattern" in file1.txt
grep -f patterns.txt file1.txt # searches for lines in file1.txt that match any of the patterns listed in patterns.txt
grep --color=auto "search_term" file1.txt # highlights matching terms in the output
grep -R "search_term" /path/to/directory/ | less # searches for "search_term" in all files within the specified directory and its subdirectories, and displays the results one page at a time
grep -R --exclude-dir="relative_dir_to_exclude" "search_term" /path/to/directory/ # searches for "search_term" in all files within the specified directory and its subdirectories, excluding the specified directory
grep -R --include="*.txt" "search_term" /path/to/directory/ # searches for "search_term" in all .txt files within the specified directory and its subdirectories
grep -R --exclude="*.log" "search_term" /path/to/directory/ # searches for "search_term" in all files within the specified directory and its subdirectories, excluding .log files
grep -R --exclude-dir={dir1,dir2} "search_term" /path/to/directory/ # searches for "search_term" in all files within the specified directory and its subdirectories, excluding multiple specified directories
grep -R --include={*.txt,*.md} "search_term" /path/to/directory/ # searches for "search_term" in all .txt and .md files within the specified directory and its subdirectories
grep -R --exclude-dir={dir1,dir2} --include={*.txt,*.md} "search_term" /path/to/directory/ # searches for "search_term" in all .txt and .md files within the specified directory and its subdirectories, excluding multiple specified directories
find /path/to/directory/ -name "file1.txt" # searches for a file named file1.txt within the specified directory and its subdirectories
find /path/to/directory/ -type f -name "*.txt" # searches for all files with a .txt extension within the specified directory and its subdirectories
find /path/to/directory/ -type d -name "subdir" # searches for all directories named subdir within the specified directory and its subdirectories
find /path/to/directory/ -type f -size +1M # searches for all files larger than 1 megabyte within the specified directory and its subdirectories
find /path/to/directory/ -type f -mtime -7 # searches for all files modified within the last 7 days within the specified directory and its subdirectories
find /path/to/directory/ -type f -perm 644 # searches for all files with permissions set to 644 within the specified directory and its subdirectories
find /path/to/directory/ -type f -exec grep "search_term" {} \ # searches for "search_term" in all files within the specified directory and its subdirectories, executing grep on each file found   
which command_name # shows the full path of the specified command
. # Alias for the current directory, used to execute scripts in the current shell environment
.. # Alias for the parent directory, used to navigate up one level in the directory structure
shebang # The first line of a script that indicates which interpreter should be used to execute the script eg. #!/usr/bin/env bash
export VARIABLE_NAME=value # sets an environment variable that can be accessed by child processes that does not persist after the shell session ends
unset VARIABLE_NAME # removes an environment variable from the current shell session
set # displays the names and values of all shell variables and functions in the current shell session
--help # displays a help message for a command, showing its usage and available options
wc # counts the number of lines, words, and characters in a file
wc -l file1.txt # counts the number of lines in file1.txt
wc -c file1.txt # counts the number of characters in file1.txt
wc -w file1.txt # counts the number of words in file1.txt
wc -L file1.txt # prints the length of the longest line in file1.txt
wc -m file1.txt # counts the number of characters in file1.txt, including multibyte characters
wc -l -w -c file1.txt # counts the number of lines, words, and characters in file1.txt and prints them in a single line
$? # prints the exit status of the last command executed, where 0 indicates success and any non-zero value indicates an error
command1 ; command2 # executes command1 and then command2, regardless of whether command1 succeeds or fails
command1 && command2 # executes command2 only if command1 succeeds (exit status 0)
command1 || command2 # executes command2 only if command1 fails (non-zero exit status)
stdout # standard output, the default destination for output from commands, usually the terminal
stderr # standard error, the default destination for error messages from commands, usually the terminal
stdin # standard input, the default source of input for commands, usually the keyboard
read variable_name # reads a line of input from the user and assigns it to the specified variable
read -p "Enter your name: " name # prompts the user for input and assigns it to the variable name
read -s -p "Enter your password: " password # prompts the user for input without echoing it to the terminal, useful for passwords
read -n 1 -p "Press any key to continue..." # waits for the user to press a single key before continuing
read -t 5 -p "Enter your name (you have 5 seconds): " name # waits for the user to enter input for 5 seconds, after which it continues without input
read -a array_name # reads a line of input and splits it into an array, assigning it to the specified array variable
read -d '' variable_name # reads input until a null character is encountered, useful for reading multi-line input
read -e variable_name # allows the user to use readline features (like arrow keys) when entering input
read -i "default_value" variable_name # provides a default value for the input prompt, which the user can edit
read -r variable_name # reads input without interpreting backslashes as escape characters
read  # waits for the user to press Enter before continuing, without assigning input to a variable
| # pipes the output of one command as input to another command
sudo apt install package_name # installs a package using the apt package manager with superuser privileges
sudo apt update # updates the package lists for upgrades and new package installations
sudo apt upgrade # upgrades all installed packages to their latest versions
sudo apt remove package_name # removes a package using the apt package manager with superuser privileges
sudo apt update && sudo apt upgrade -y # updates the package lists and upgrades all installed packages without prompting for confirmation
apt --version # displays the version of the apt package manager installed on the system
sudo apt install neovim # installs the neovim text editor using the apt package manager with superuser privileges
nvim --version # displays the version of neovim installed on the system
nano file1.txt # opens file1.txt in the nano text editor for editing ctrl+O to save, ctrl+X to exit
vim file1.txt # opens file1.txt in the vim text editor for editing
man command_name # displays the manual page for the specified command, showing its usage, options, and examples
ln -s target_file link_name # creates a symbolic link named link_name that points to target_file
top # displays a dynamic, real-time view of system processes and resource usage M to sort by memory usage, P to sort by CPU usage, q to quit
htop # an interactive process viewer that provides a more user-friendly interface than top
ps aux # displays a snapshot of all running processes with detailed information such as user, PID, CPU and memory usage
kill PID # sends a termination signal to the process with the specified PID 
ps aux | grep "process_name" # searches for a process by name and displays its details
killall process_name # sends a termination signal to all processes with the specified name
ps grep "process_name" # searches for a process by name and displays its details
chmod permissions file_name # changes the permissions of a file or directory, where permissions can be specified in symbolic (e.g., u+x) or numeric (e.g., 755) format
chmod -R permissions directory_name # changes the permissions of a directory and all its contents recursively
chown user:group file_name # changes the ownership of a file or directory to the specified user and group
chown -R user:group directory_name # changes the ownership of a directory and all its contents recursively
chmod u+x script.sh # adds execute permission for the user on script.sh
chmod g-w file.txt # removes write permission for the group on file.txt
chmod o+r file.txt # adds read permission for others on file.txt
chmod u=rw,g=r,o= file.txt # sets user permissions to read/write, group permissions to read-only, and removes all permissions for others on file.txt
chmod +x script.sh # adds execute permission for all users on script.sh
chmod 777 file.txt # sets read, write, and execute permissions for user, group, and others on file.txt read = 4, write = 2, execute = 1, so 7 = 4+2+1
#Install Webi to perform lsd commands
curl -sS https://webi.sh/lsd | sh # installs lsd, a modern replacement for the ls command, using a shell script from the specified URL
source ~/.config/envman/PATH.env # reloads the PATH environment variable from the specified file, allowing changes to take effect in the current shell session
lsd --classic # lists files and directories in the current working directory using the lsd command with the classic theme
lsd --theme=default # lists files and directories in the current working directory using the lsd command with the default theme
lsd --theme=dracula # lists files and directories in the current working directory using the lsd command with the dracula theme
lsd --theme=solarized # lists files and directories in the current working directory using the lsd command with the solarized theme
lsd --theme=monokai # lists files and directories in the current working directory using the lsd command with the monokai theme
lsd --theme=one-dark # lists files and directories in the current working directory using the lsd command with the one-dark theme
lsd --theme=one-light # lists files and directories in the current working directory using the lsd command with the one-light theme
lsd --theme=material # lists files and directories in the current working directory using the lsd command with the material theme
lsd --theme=ayu # lists files and directories in the current working directory using the lsd command with the ayu theme
lsd --theme=tomorrow-night # lists files and directories in the current working directory using the lsd command with the tomorrow-night theme
lsd --theme=tomorrow-day # lists files and directories in the current working directory using the lsd command with the tomorrow-day theme
lsd --theme=solarized-dark # lists files and directories in the current working directory using the lsd command with the solarized-dark theme
lsd --theme=solarized-light # lists files and directories in the current working directory using the lsd command with the solarized-light theme
lsd --theme=gruvbox-dark # lists files and directories in the current working directory using the lsd command with the gruvbox-dark theme
lsd --theme=gruvbox-light # lists files and directories in the current working directory using the lsd command with the gruvbox-light theme
lsd --theme=gruvbox-material # lists files and directories in the current working directory using the lsd command with the gruvbox-material theme
lsd --theme=gruvbox-contrast # lists files and directories in the current working directory using the lsd command with the gruvbox-contrast theme
lsd --theme=gruvbox # lists files and directories in the current working directory using the lsd command with the gruvbox theme
lsd --tree # lists files and directories in the current working directory in a tree-like format using the lsd command
lsd --group-dirs=first # lists files and directories in the current working directory using the lsd command, with directories displayed before files
lsd --icon=always # lists files and directories in the current working directory using the lsd command, always displaying icons next to file names
lsd --icon=never # lists files and directories in the current working directory using the lsd command, never displaying icons next to file names
lsd --icon=auto # lists files and directories in the current working directory using the lsd command, displaying icons next to file names only when the output is a terminal
lsd --color=always # lists files and directories in the current working directory using the lsd command, always displaying colored output
lsd --color=never # lists files and directories in the current working directory using the lsd command, never displaying colored output
lsd --color=auto # lists files and directories in the current working directory using the lsd command, displaying colored output only when the output is a terminal
curl -L https://example.com/file.zip -o file.txt # This command uses curl to download a file from the specified URL (https://example.com/file.zip) and saves it as file.txt in the current directory. The -L option tells curl to follow any redirects that may occur during the download process.
curl https://example.com                    # fetch a URL and print the response to the terminal
curl -O https://example.com/file.txt        # download and save it as file.txt (keeps the original filename)
curl -o myname.txt https://example.com/f.txt # download and save it under a custom filename
curl -sS https://webi.sh/lsd | sh           # download a script and pipe it straight into sh to run it (this is how you installed lsd)
curl -I https://example.com                 # fetch only the response headers (no body) — useful for checking if a URL is alive
curl -L https://example.com                 # follow redirects (some URLs redirect elsewhere; -L makes curl follow along)
history -c    # clear in-memory
history -w    # write the (now empty) history out, overwriting ~/.bash_history
> ~/.bash_history # (empties the file without deleting it) 
rm ~/.bash_history # (deletes it entirely — bash recreates it next time it needs to write history).
history                # find the line number of the entry
history -d <line_number>  # delete just that one entry
history -w              # save the change to disk
!<history_number>          # re-run a command from history by its number
!<prefix>                  # re-run the most recent command that starts with <prefix>
!<program_name>              # re-run the most recent command that starts with <program_name>
!<prefix>:p                    # print what it WOULD run, without executing it (safety check before you trust it)
alias                              # list all saved aliases
alias gs='git status'               # creates a shortcut command gs that runs git status
unalias gs                           # removes the alias gs
echo "alias gs='git status'" >> ~/.bashrc # adds the alias gs='git status' to your ~/.bashrc file so that it persists across shell sessions
source ~/.bashrc                            # reloads the ~/.bashrc file to apply any changes made to it
# alias.sh contains: alias gs='git status'
bash alias.sh    # runs it in a child process -- gs alias is gone the instant this finishes; useless here
source alias.sh   # runs it in YOUR shell -- gs alias now works from this point on, in this terminal
    # - source alias.sh is functionally identical to having pasted the contents of alias.sh straight into ~/.bashrc 
echo 'source ~/alias.sh' >> ~/.bashrc # add ~/alias.sh into ~/.bashrc    
# Create an archive
tar -cvf archive.tar files/or/dirs
tar -czvf archive.tar.gz files/or/dirs    # gzip compressed
# Extract an archive
tar -xvf archive.tar
tar -xzvf archive.tar.gz                  # gzip compressed
tar -xzvf archive.tar.gz -C /target/dir   # extract to specific directory
# List contents without extracting
tar -tvf archive.tar.gz
# Flags:
  - c = create, x = extract, t = list/table
  - z = gzip (.tar.gz/.tgz); use j for bzip2 (.tar.bz2), J for xz (.tar.xz)
  - v = verbose (show files as processed)
  - f = filename follows (almost always needed, goes last before the filename)
# If you're pulling a .tar.gz down and just want a quick "unpack this" command, it's:
  tar -xzvf filename.tar.gz