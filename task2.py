# 2. Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1) для перебора ip-адресов из заданного диапазона. 
# Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.

from ipaddress import ip_address
from task1 import hostPing

def hostRangePing(for3task=False):
    startAddr = ip_address(input('Insert first IP: '))
    while True:
        numberOfIPs = int(input('Insert count of IP addresses to check: '))
        if (int(str(startAddr).split('.')[-1]) + numberOfIPs) > 255:
            maxCount = 255 - int(str(startAddr).split('.')[-1])
            print('Last octet can not be greater then 255, try again')
            print(f'hint - with first IP {startAddr} you can check {maxCount} addresses maximum')
        else:
            break
    hostList = []
    currAddr = startAddr
    for i in range(0, numberOfIPs):
        hostList.append(str(currAddr))
        currAddr += 1
        i += 1

    if for3task:
        hostPing(hostList, for3task=True)
        from task1 import reachableList, unreachableList
        return reachableList, unreachableList
    else:
        hostPing(hostList)


