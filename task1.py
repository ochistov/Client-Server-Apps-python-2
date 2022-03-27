import subprocess
import threading, os, socket, platform, re

reachableList = []
unreachableList = []

def ping(host, for3task=False):
    DNULL = open(os.devnull, 'w')
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    if re.match('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', str(host)):
            ipAddr = str(host)
    else:
        try:
            ipAddr = socket.gethostbyname(host)
        except:
            print(f'Hostname {host} is incorrect! {host} is unreachable')
            return
    response = subprocess.call(['ping', param, '2', ipAddr], stdout=DNULL)
    if response == 0:
        if for3task:
            reachableList.append(host)
        else:
            print(f'{host} is reachable!')
        

    else:
        if for3task:
            unreachableList.append(host)
        else:
            print(f'{host} is unreachable!')
        

def hostPing(hostList, for3task=False):
    numThreads = int(len(hostList))
    number = 0
    while number < len(hostList):
        for i in range(numThreads):
            if for3task:
                t = threading.Thread(target=ping, args=(hostList[number + i], True,))
                t.start()
            else:
                t = threading.Thread(target=ping, args=(hostList[number + i],))
                t.start()
        t.join()
        number = number + numThreads