import ldap3

server = ldap3.Server('10.10.10.119', get_info = ldap3.ALL, port=389, use_ssl=True)
conn = ldap3.Connection(server)
conn.bind()

print(server.info)
