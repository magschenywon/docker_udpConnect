from socket import *
from time import ctime,sleep
sleep(3)
hosts = "localhost"
port = 5678
addr = (hosts, port)
usc = socket(AF_INET, SOCK_DGRAM)
i = 0
while True:
    usc.sendto(str(i).encode(), addr)
    data,adds = usc.recvfrom(1024)
    if not data: break
    i += 1
    print (i, adds,data.decode())
    sleep(5)
usc.close()
