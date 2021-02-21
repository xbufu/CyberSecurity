# Enumeration

- Found book store app running in `/store`

# RCE

- Could get RCE with known exploit for book store

	`https://www.exploit-db.com/exploits/47887`

# PrivEsc

- Found credentials for user `tony` in `/home/tony/password.txt`

	`tony:yxcvbnmYYY`

- Was able to get root with `sudo`

	`sudo pkexec /bin/sh`
