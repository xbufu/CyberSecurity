# Enumeration

## Web server on port 80

- Service information

	`nginx 1.16.1`

- Found admin login

	`/admin/login/?next=/admin/`

## Web server on port 8000

- Service information
	
	```
	nginx 1.16.1
	CherryPy 5.6.0
	```

- Found interesting header hinting to another application

	`Saltstack 3000.1`

# RCE

- Could get root shell with known exploit

	`https://github.com/jasperla/CVE-2020-11651-poc`
