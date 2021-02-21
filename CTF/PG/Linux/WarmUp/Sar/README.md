# Enumeration

## Web server on port 80

- Found entry in `/robots.txt`

	`sar2HTML`

- Found service information

	`sar2HTML 3.2.1`

# RCE

- Could get RCE with command injection at

	`http://sar.pg/sar2HTML/index.php?plot=;id`

# PrivEsc

- Found crontab running script as root
