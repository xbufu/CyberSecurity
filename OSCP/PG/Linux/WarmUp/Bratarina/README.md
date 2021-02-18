# Enumeration

## Web server port 80

- Service information

	`nginx 1.14.0`

## Netbios/SMB port 445

- Service information

	`Samba smbd 4.7.6-Ubuntu`

- Found file `passwd.bak` containing a backup of /etc/passwd

- Found username 

	`neil`

## SMTP on port 25

- Service information

	`OpenSMTPD 2.0.0`

- Possible exploit

	`CVE-2020-7247`

# RCE & PrivEsc

- Got root shell with exploit for OpenSMTPD
