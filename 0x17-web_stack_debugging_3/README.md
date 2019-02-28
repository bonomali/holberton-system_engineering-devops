# 0x17. Web Stack Debugging 3
---
## Description

During this project I will learn:
- Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to master it. In this debugging series, broken/bugged webstacks will be concocted and the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state.
---

## Requirements

- All files will be interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All Bash script files must be executable
- Puppet manifests must pass `puppet-lint` without any errors (version 2.1.1):
- Puppet manifests must run without error
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Puppet manifest files must end with the extension `.pp`
- Files will be checked with Puppet v3.4


---
File|Task
---|---
0-strace_is_your_friend.pp | Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing)

## Author
Essence Boayue [Github](https://github.com/eboayue)|[LinkedIn](https://www.linkedin.com/in/essenceboayue/)|[Twitter](https://twitter.com/girlsaregeeks2)
