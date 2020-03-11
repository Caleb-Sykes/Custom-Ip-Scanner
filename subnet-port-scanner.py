from datetime import date
import socket
import os

# DEFINITIONS ----------------------------------------------------------
def subnet_generator(file_name):
    file = open(file_name,"w+")
    for ip in range(0,254):
        if ip > 10 and ip % 2 == 1:
            file.write("172.27.56."+str(ip)+".\n")
    file.close()

def portscanner(file_name,port1,port2):
    today = date.today()
    print("[*] Starting Port Scan")
    try:
        file2 = open("Scan_Report.txt","w+")
        file2.write("[*] Port Scan Results ========================== ["+today.strftime("%d/%m/%Y")+"]\n")
        with open(file_name,'r+') as file:
            ips = file.readlines()
            for ip in ips:
                for port in range(int(port1),int(port2)):
                    ping = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    ping.settimeout(0.2)
                    data = ping.connect_ex((str(ip[:-2]),int(port)))
                    if data == 0:
                        file2.write("[+]  "+str(port)+": "+str(ip[:-2])+"\n")
                        print("[+]  "+str(port)+": "+str(ip[:-2]))
        file2.close()
        file.close()
        os.remove("Saved_IPS.txt")
    except KeyboardInterrupt:
        print("[-] Exiting Portscanner: Keyboard Interrupt"+"\n"+"(: Bye!")
        exit()

# SEQUENCES ------------------------------------------------------------
subnet_generator("Saved_IPs.txt")
print("Calebs Portscanner !!\n")
print("disclaimer: big ranges may take a while")
print("\n[!] The first 10 IP Adresses are reserved for printers")

descision = input("Will you be scanning a range(r) or 1 port(1)? (r/1): ")

if descision == "r":
    port1 = input("First port in the range: ")
    port2 = input("Second port in the range: ")
    portscanner("Saved_IPs.txt",int(port1),int(port2))
elif descision == "1":
    port = input("Port to scan for: ")
    portscanner("Saved_IPs.txt",int(port),(int(port)+1))

print("[*] Port Scan Finished Successfully!")
print("[!] View Scan_Report.txt in for results (will reside in the script's path)")
