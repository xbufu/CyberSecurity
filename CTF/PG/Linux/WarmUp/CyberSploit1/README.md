# Enumeration

## Web server on port 80

- Service information

	`Apache httpd 2.2.22 ((Ubuntu))`

- Found username in source of `/index.html`

	`itsskv`

- Found base64 encoded string in `robots`

	`Y3liZXJzcGxvaXR7eW91dHViZS5jb20vYy9jeWJlcnNwbG9pdH0=`

- Decoded to 

	`cybersploit{youtube.com/c/cybersploit}`

# RCE

- Could login to SSH

	`itsskv:cybersploit{youtube.com/c/cybersploit}`

# PrivEsc

- Found old kernel and OS version

	`https://www.exploit-db.com/exploits/37292`
