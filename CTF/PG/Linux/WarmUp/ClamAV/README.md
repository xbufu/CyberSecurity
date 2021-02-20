# Enumeration

## Web server on port 80

- Service information

	`Apache httpd 1.3.33 ((Debian GNU/Linux))`

- Possible exploit from `searchsploit`

	`Apache 1.3.x mod_mylo - Remote Code Execution | multiple/remote/67.c`

- Found binary string on homepage

	`01101001 01100110 01111001 01101111 01110101 01100100 01101111 01101110 01110100 01110000 01110111 01101110 01101101 01100101 01110101 01110010 01100001 01101110 00110000 0011 0000 01100010`

## SMB on port 139/445

- Service information

	`Samba 3.0.14a-Debian`

- Found usernames

	```
	root
	ryu
	nobody
	www-data
	```

## Smux on port 199

- Service information

	`Linux SNMP multiplexer`

- Found another IP address

	`192.168.119.254`

- Found possible open UDP ports

	```
	137
	138
	161
	```

## SNMP on UDP port 161

- Service information

	`SNMPv1 server; U.C. Davis, ECE Dept. Tom SNMPv3 server (public)`

- Found `clamav` service running

# RCE

- Could get root shell through exploit for `clamav` and `Sendmail SMTP`

	`CVE-2007-4560 https://www.exploit-db.com/exploits/4761`
