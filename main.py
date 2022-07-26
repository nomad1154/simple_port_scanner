import socket
import sys

target = input("Define Target")
portmin = input("Define starting port")
portmax = input("Define ending port")
targetv4 = socket.gethostbyname(target)

print("-" * 50)
print("Target: " + targetv4)
print(f"Scanning ports {portmin}-{portmax}")
print("-" * 50)

portlist = []

portminint = int(portmin)
portmaxint = int(portmax)
try:
    for port in range(portminint, portmaxint):
       print(f"Scanning Port {port}")
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       socket.setdefaulttimeout(0.2)
       result = s.connect_ex((target,port))
       if result ==0:
           portlist.append(port)
           print(f"Found open port {port}")
       s.close()

except KeyboardInterrupt:
    print("Error")
    sys.exit()
except socket.error:
    print("Error")
    sys.exit()
portliststr = str(portlist)

print("-" * 50)
print("Scanning Complete...")
print("Open Ports: " + portliststr)
print("Target Web Address: " + target)
print("Target IPv4 Address: " + targetv4)
print("-" * 50)







