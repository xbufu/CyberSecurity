# Enumeration

## FTP on port 21

- Service information

	`vsftpd 3.0.3`

- Anonymous login allowed

- Got possible usernames from file

	```
	Anurodh
	Apaar
	```

## Web server on port 80

- Service information

	`Apache httpd 2.4.29`

- Found directory where you can execute commands

	`/secret`

- Could bypass filter with single quotes

- Found more users

	```
	aurick
	apaar
	anurodh
	```

# RCE

- Got reverse shell with command filter bypass

# PrivEsc

- Found MySQL credentials in `/var/www/files/index.php`

	`root:!@m+her00+@db`

- Found hashes from MySQL

	```
	anurodh:7e53614ced3640d5de23f111806cc4fd
	apaar:686216240e5af30df0501e53c789a649
	```

- Cracked hashes

	```
	anurodh:masterpassword
	apaar:dontaskdonttell
	```
