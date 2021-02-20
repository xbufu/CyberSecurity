# Enumeration

## Web server on port 80

- Found service and version from error page

	`nginx 1.10.3`

## Web server on port 8080

- Running `NodeBB` forum software

- Possible account takeover exploit

	`https://www.exploit-db.com/exploits/48875`

- 3 entries in `/robots.txt`

- Local login disabled

## Redis on port 6379

- Service information

	`Redis 5.0.9`

- Anonymous login allowed

## MongoDB on port 27017

- Service information

	`MongoDB 4.0.18`

# RCE

- Could get reverse shell as root through redis

