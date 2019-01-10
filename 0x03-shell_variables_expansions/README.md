# 0x03-Shell Variables and Expansions
---

## Description

During this project I will learn:
- Shell initialization files
	* What are the `/etc/profile` file and the `/etc/profile.d` directory
	* What is the `~/.bashrc` file
- Variables
	* What is the difference between a local and a global variable
	* What is a reserved variable
	* How to create, update and delete shell variables
	* What are the roles are the following reserved variables: HOME, PATH, PS1
	* What are special parameters
	* What is the special parameter `$?`?
- Expansions
	* What is expansion and how to use them
	* What is the difference between single and double quotes and how to use them properly
	* How to do command substitution with `$()` and backticks
- Expansions & Shell Arithmetic
	* How to perform arithmetic operations with the shell
- The alias Command
	* How to create an alias
	* How to list aliases
	* How to temporarily disable an alias
- Other help pages
	* How to execute commands from a file in the current shell
- And
	* What happens when you type `$ ls -l *.txt`
---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All scripts will be tested on Ubuntu 14.04 LTS
- All scripts should be exactly two lines long (`$ wc -l` file should print 2)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- Not allowed to use backticks, `&&`, `||` or `;`
- Not allowed to use `bc`, `sed` or `awk`
- All scripts must be executable.
---

File|Task
---|---
0-alias |  a script that creates an alias.
1-hello_you | a script that prints `hello user`, where user is the current Linux user.
2-path | Add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program
3-paths | a script that counts the number of directories in the `PATH`
4-global_variables | a script that lists environment variables.
5-local_variables | a script that lists all local variables and environment variables, and functions
6-create_local_variable | a script that creates a new local variable.
7-create_global_variable | a script that creates a new global variable.
8-true_knowledge | a script that prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line
9-divide_and_rule | a script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line.
10-love_exponent_breath | a script that displays the result of `BREATH` to the power `LOVE`
11-binary_to_decimal | a script that converts a number from base 2 to base 10
12-combinations | a script that prints all possible combinations of two letters, except `oo`
13-print_float | a script that prints a number with two decimal places.
14-decimal_to_hexadecimal | a script that converts a number from base 10 to base 16.
15-blog post | [What happens when use ls*.c in the shell](https://medium.com/@girlsaregeeks2/what-happens-when-you-use-ls-c-in-the-shell-3c643f907410)


## Author
Essence Boayue [Github](https://github.com/eboayue)|[LinkedIn](https://www.linkedin.com/in/essenceboayue/)|[Twitter](https://twitter.com/girlsaregeeks2)
