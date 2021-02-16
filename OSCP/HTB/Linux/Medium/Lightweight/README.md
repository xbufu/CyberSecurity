# Enumeration

## Web Server

- Protected against directory brute forcing

- From `user.php` found that we can access machine by SSH with our IP as user and password

## LDAP

- Got hashes with nmap script

	```
	ldapuser1:$6$3qx0SD9x$Q9y1lyQaFKpxqkGqKAjLOWd33Nwdhj.l4MzV7vTnfkE/g/Z/7N5ZbdEQWfup2lSdASImHtQFh6zMo41ZA./44
	ldapuser2:$6$xJxPjT0M$1m8kM00CJYCAgzT4qz8TQwyGFQvk3boaymuAmMZCOfm3OA7OKunLZZlqytUp2dun509OBE2xwX/QEfjdRQzgn
	```

- Unable to crack hashes

- Can sniff for traffic on victim with tcpdump for credentials since SSL not used

	`ldapuser2:8bc8251332abe1d7f105d3e53ad39ac2`

- Found encrypted 7z file

- Could convert it to hash with 7z2john and crack with hashcat

	`delete`

- Found credentials in `status.php`

	`ldapuser1:f3ca9d298a553da117442deeb6fa932d`


