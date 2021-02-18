# Enumeration

## Web Server

- Found possible usernames

	```
	admin
	oscp
	```

- Website running wordpress 5.4.2

- 1 disallowed entry in in `/robots.txt`

	`/secret.txt`

- Contains base64 encoded string

- Decodes to SSH key

# RCE

- Could login to machine with ssh key and user `oscp`

# PrivEsc

- Found `/usr/bin/bash` had SGID bit set and was owned by `root:root`
