# 0x00. Bash - Shell, basics
---
## Description

During this project I will learn:
- What Is “The Shell”?
	* What is the difference between a terminal and a shell
	* What is the shell prompt
	* How to use the history (the basics)
- Navigation
	* What do the commands or built-ins `cd`, `pwd`, `ls` do
	* How to navigate the filesystem
	* What are the . and .. directories
	* What is the working directory, how to print it and how to change it
	* What is the root directory
	* What is the home directory, and how to go there
	* What is the difference between the root directory and the home directory of the user root
	* What are the characteristic of hidden files and how to list them
	* What does the command `cd` - do
- Looking Around
	* What do the commands `ls`, `less`, `file` do
	* How do you use options and arguments with commands
	* Understand the ls long format and how to display it
- A Guided Tour
	* What does the `ln` command do
	* What do you find in the most common/important directories
	* What is a symbolic link
	* What is a hard link
	* What is the difference between a hard link and a symbolic link
- Manipulating Files
	* What do the commands `cp`, `mv`, `rm`, `mkdir` do
	* What are wildcards and how do they work
	* How to use wildcards
- Working With Commands
	* What do `type`, `which`, `help`, `man` commands do
	* What are the different kinds of commands
	* What is an alias
	* When do you use the command help instead of man
- Reading Man Pages
	* How to read a man page
	* What are man page sections
	* What are the section numbers for User commands, System calls and Library functions
- Keyboard shortcuts for Bash
	* Common shortcuts for Bash
- LTS
	* What does `LTS` mean?
- Other
	* What does RTFM mean?
	* What is a Shebang
---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All scripts will be tested on Ubuntu 14.04 LTS
- All scripts should be exactly two lines long (`$ wc -l` file should print 2)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- Not allowed to use backticks, `&&`, `||` or `;`
- All scripts must be executable. Use this command: `chmod u+x file`.
---

File|Task
---|---
0-current_working_directory | a script that prints the absolute path name of the current working directory
1-listit | Display the contents list of your current directory
2-bring_me_home | a script that changes the working directory to the user’s home directory
3-listfiles| Display current directory contents in a long format
4-listmorefiles | Display current directory contents, including hidden files (starting with `.`). Use the long format.
5-listfilesdigitonly | Display current directory contents: Long format, with user and group IDs displayed numerically, and hidden files (starting with `.`)
6-firstdirectory| a script that creates a directory named `holberton` in the `/tmp/` directory.
7-movethatfile | Move the file `betty` from `/tmp/` to `/tmp/holberton`
8-firstdelete | Delete the file `betty`
9-firstdirdeletion | Delete the directory `holberton` that is in the `/tmp directory`.
10-back | a script that changes the working directory to the previous one
11-lists | a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.
12-file_type | a script that prints the type of the file named `iamafile`. The file `iamafile` will be in the `/tmp` directory when we will run your script
13-symbolic_link | a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory
14-copy_html | a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
15-lets_move |  a script that moves all files beginning with an uppercase letter to the directory `/tmp/u`
16-clean_emacs | a script that deletes all files in the current working directory that end with the character `~`
17-tree | a script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/holberton` in the current directory
18-commas | a command that lists all the files and directories of the current directory, separated by commas. Directory names should end with a slash. Files and directories starting with a dot should be listed. The listing should be alpha ordered, except for the directories `.` and `..` which should be listed at the very beginning. Only digits and letters are used to sort; Digits should come first. Assume that all the files we will test with will have at least one letter or one digit. The listing should end with a new line
holberton.mgc | a magic file `holberton.mgc` that can be used with the command `file` to detect `Holberton` data files. `Holberton` data files always contain the string `HOLBERTON` at offset 0.

## Author
Essence Boayue [Github](https://github.com/eboayue)|[LinkedIn](https://www.linkedin.com/in/essenceboayue/)|[Twitter](https://twitter.com/girlsaregeeks2)
