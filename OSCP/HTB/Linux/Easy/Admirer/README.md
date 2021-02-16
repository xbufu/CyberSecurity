# Enumeration

## Web server on port 80

- Found entry and possible username in `/robots.txt`

	`/admin-dir`

	`waldo`

- Could access `/admin/contacts.txt` and got usernames and emails
	
	- Admins:

		`penny 		- 	p.wise@admirer.htb`
	
	- Developers:

		```
		rajesh 		- 	r.nayyar@admirer.htb
		amy 		- 	a.bialik@admirer.htb
		leonard 	-	l.galecki@admirer.htb
		```

	- Designers

		```
		howard		-	h.helberg@admirer.htb
		bernadette	-	b.rauch@admirer.htb
		```

- Could access `/admin-dir/credentials.txt` and got credentials

	- Internal mail account
	
		w.cooper@admirer.htb:fgJr6q#S\W:$P

	- FTP account

		ftpuser:%n?4Wz}R$tTF7

	- Wordpress account

		admin:w0rdpr3ss01!

- Could access FTP server with credentials and got SQL dump and mirror of the website

- Got database type and version from `dump.sql`

	`MariaDB 10.1.41`

- Got credentials from `index.php`

	`waldo:]F7jLHw:*G>UPrTo}~A"d6b`

- Got credentials from `utility-scripts/db_admin.php`

	`waldo:Wh3r3_1s_w4ld0?`


