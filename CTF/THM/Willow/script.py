char_list = []

d = 61527
mod = 37627

print("[+] Starting the decryption process")

with open("ciphertext", "r") as ciphertext:
    for line in ciphertext:
        char_list += [chr((int(x) ** d) % mod) for x in line.strip().split(' ')]

print("[+] Successfully decrypted ... Storing in 'ssh_key'")

with open("ssh_key", "w") as willow_key:
    willow_key.write(''.join(char_list))

print("[+] Done")
