# Enumeration

# Web server on port 80

- Service information

	`Node.js Express`

- Got list of usernames from homepage

	```
	rosalinda
	refugio
	rachael
	israel
	catherine
	gavin
	james
	nina
	carole
	ernie
	```

- Found api access at `/api`

- Valid api queries

	```
	users
	settings
	backup?filename=
	```

- Could get list of users from api at `/api/users`

- Fuzzed login request and found working credentials

	```
	dev-acct:password
	```

- Could access `/api/settings` now

- Saw there was a parameter to set admin user

- Could intercept request for changing theme and get admin user for website

# RCE

- Could get command injection through backup creation input
