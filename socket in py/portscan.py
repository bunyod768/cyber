import socket

def scan_ports(target):
    print(f"[STARTING SCAN] Target: {target}")
    for port in range(1, 1001):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open")
        s.close()


target_ip = input("IP yoki domen kiriting: ")  
scan_ports(target_ip)
