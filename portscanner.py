import socket
target = ('192.168.0.21')
for i in range(1,251):
    ping = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data = ping.connect_ex((target,i))
    if data == 0:
        print("[+] Port",i)
print("[.] Scan Finished Successfully")
