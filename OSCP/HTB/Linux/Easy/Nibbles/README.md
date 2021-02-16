# Scanning & enumeration

## Rustscan

- Found port 22 & 80

- Web server running Apache httpd 2.4.18 Ubuntu

## Web Server

- Found comment in source hinting to new directory

	`/nibbleblog`

- Found service and version of blog from `/nibbleblog/update.php`

	`Nibbleblog 4.0.3 "Coffee" 2009-2014`

- Could access config file at `/nibbleblog/content/private/config.xml`

- Found admin login panel at `/nibbleblog/admin.php`

- Blacklist protection against brute force attacks

- Got custom list with CeWL

- Found working credentials

	`admin:nibbles`

# RCE

- Was able to upload a reverse shell and get RCE with `CVE-2015-6947`

# Privilege Escalation

- Could run editable script with sudo
