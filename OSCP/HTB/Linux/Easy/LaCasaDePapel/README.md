# Scanning & Enumeration

- Found SHA-1 secret from QR Code

	`EN2UYYK2NV3UQQLNKBCWKV2HPFADA4SJ`

- Found backdoor exploit for FTP

- Got usernames

	```
	berlin
    dali
    nairobi
    oslo
    professor
	```

- Got private key for SSL

	`/home/nairobi/ca.key`

- Generated self-signed certificate

	```
	openssl req -new -x509 -nodes -days 365 -key ca.key -out ca.pem
	openssl pkcs12 -export -out bufu.pfx -inkey ca.key -in ca.pem
	```

- Found file path was base64 encrypted

- Found ssh key in berlin for professor

- Linpeas:

	/media/usb
	Service running on 11211

- Could get root by putting reverse shell into /home/professor/memcached.ini
