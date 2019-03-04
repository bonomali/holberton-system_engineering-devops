# 0x19. Postmortem
---
## Issue Summary:
Monday, March 4th from 11am to 2pm PT, our website was down. 100% of users were experiencing 500 errors when attempting to load the web page, and thereby could not use the site. The root cause was found to be a misconfigured Wordpress configuration file. There was a typo in the wp-settings.php file where an engineer put “phpp” instead of “php” as the file extension for one setting. Because of that, Wordpress could not properly load.
- Timeline
	* Detected at 11 am PT
	* How was it detected: Sumologic monitoring detected the 500 error when it happened
	* Actions taken: Engineers confirmed site was down, investigated using strace, and fixed the error via Puppet script
	* Misleading paths: Engineers saw some file not found errors using strace, thought required files were missing until it was found that all of those errors were stemming from the typo in the config file
	* Which team handled it: SRE
- Corrective/preventative measures:
	* Restrict push to production access to certain team leads
	* Enforce careful screening of all pull requests to catch things like this in future
	* Create unittests for the codebase
