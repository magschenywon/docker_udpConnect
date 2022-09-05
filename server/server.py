from socket import *
from time import ctime,sleep
hosts = ''
port = 5678
addr = (hosts, port)
uss = socket(AF_INET, SOCK_DGRAM)
uss.bind(addr)
i = 0
while True:
    print ('udp Server waiting')
    data,addc = uss.recvfrom(1024)
    if not data: break
    i += 1
    print (data.decode(), addc)
    sleep(5)
    uss.sendto(str(ctime()).encode(), addc)

uss.close()

