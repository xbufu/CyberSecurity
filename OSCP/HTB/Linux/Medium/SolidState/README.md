# Enumeration

## Web Server on port 80

- Found email on main page

	`webadmin@solid-state-security.com`

## SMTP on port 25

- Could connect through telnet and got service information
	
	`JAMES SMTP Server 2.3.2`

## Administration interface for JAMES on port 4555

- Could get access with default credentials and change passwords for users

	```
	root:root
	james:james
	thomas:thomas
	john:john
	mindy:mindy
	mailadmin:mailadmin
	```

- Found email in johns inbox hinting to password in mindys inbox

	`mindy:P@55W0rd1!2@`

# RCE

- Was able to SSH into the machine with mindy's credentials

- Did not get full shell but rbash

- Could escape it by providing `-t bash` to ssh command

# PrivEsc

- Found script `/opt/tmp.py` with 777 permissions that gets run by root every couple of minutes
