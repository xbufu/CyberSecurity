* Apache httpd 2.4.7 ((Ubuntu))

* Found login at /dev

* Found SQLi
	
	`admin 'or 1=1 -- -`

* Found credentials

	`admin:sup3rstr0ngp4ssf0r4d`
	`thrasivoulos:sup3rstr0ngp4ssf0r4d`

* Got RSA key

* Found SNMP running on port 161/UDP

* SNMPv1 server; net-snmp SNMPv3 server (public)

* Found IPv6 address

	`dead:beef:0000:0000:0250:56ff:feb9:d3eb`

* Found SUID /usr/local/bin/chal owned by root

* No ASLR, NX or other protections enabled

* Uses strcopy() without checking buffer size

* Got offset with gef

* Create big enough pattern to get segfault

* Got specific offset by searching for contents of `eip` (was 362)

	`pattern create 512`
	`pattern search <eip>` 

* Abused ret2libc to get root shell

* Got address of libc with

	`ldd /usr/local/bin/chal | grep libc`

* Got address of system and exit in gdb with

	`p system`
	`p exit`

* Got address of `/bin/sh` string by locating libc in memory

	`info proc map`
	`find <libc start>, <libc end>, "/bin/sh"`
