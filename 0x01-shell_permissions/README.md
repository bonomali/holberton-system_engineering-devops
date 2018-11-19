# 0x01. Bash - Shell, permissions
---

## Description

During this project I will learn:
- Permissions
	* What do the commands chmod, sudo, su, chown, chgrp do
	* Linux file permissions
	* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
	* How to change permissions, owner and group of a file
	* Why can’t a normal user chown a file
	* How to run a command with root privileges
	* How to change user ID or become superuser
- Other man pages
	* How to create a user
	* How to create a group
	* How to print real and effective user and group IDs
	* How to print the groups a user is in
---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All scripts will be tested on Ubuntu 14.04 LTS
- All scripts should be exactly two lines long (`$ wc -l` file should print 2)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- Not allowed to use backticks, `&&`, `||` or `;`
- All scripts must be executable.
---

File|Task
---|---
0-iam_betty | a script that changes your user ID to `betty`.
1-who_am_i | a script that prints the effective userid of the current user
2-groups | a script that prints all the groups the current user is part of
3-new_owner | a script that changes the owner of the file `hello` to the user `betty`
4-empty | a script that creates an empty file called `hello`
5-execute |  a script that adds execute permission to the owner of the file `hello`
6-multiple_permissions | a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file `hello`
7-everybody | a script that adds execution permission to the owner, the group owner and the other users, to the file `hello`
8-James_Bond | a script that sets the permission to the file `hello` as follows
9-John_Doe | a script that sets the mode of the file `hello` to this
10-mirror_permissions | a script that sets the mode of the file `hello` the same as `olleh’s` mode
11-directories_permissions | a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed
12-directory_permissions | a script that creates a directory called `dir_holberton` with permissions 751 in the working directory
13-change_group | a script that changes the group owner to `holberton` for the file `hello`
14-change_owner_and_group | a script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.
15-symbolic_link_permissions | a script that changes the owner and the group owner of the file `_hello` to `betty` and `holberton` respectively
16-if_only | a script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`
100-Star_Wars | a script that will play Star Wars episode IV in the terminal
101-man_holberton | a man page for `holberton`


## Author
Essence Boayue [Github](https://github.com/eboayue)|[LinkedIn](https://www.linkedin.com/in/essenceboayue/)|[Twitter](https://twitter.com/girlsaregeeks2)
d/or become the superuser
