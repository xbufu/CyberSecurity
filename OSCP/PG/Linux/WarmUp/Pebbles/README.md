# Enumeration

## FTP on port 21

- Service information 

	`vsftpd 3.0.3`

- No anonymous login allowed

## Web server on port 80

- Service information

	`Apache httpd 2.4.18`

- Found another application running in `/zm`

	`ZoneMinder 1.29`

## Web server on port 3305

- Service information

	`Apache httpd 2.4.18`

## Web server on port 8080

- Service information

	```
	Apache httpd 2.4.18
	Tomcat 9.*
	```
	
## RCE

- Found SQLi exploit for ZoneMinder 1.29

- Injectable POST parameter `limit`
