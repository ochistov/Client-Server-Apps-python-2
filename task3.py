# 3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. 
# Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате 
# (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
# Reachable

# 10.0.0.1
# 10.0.0.2
# Unreachable

# 10.0.0.3
# 10.0.0.4

from task2 import hostRangePing
from tabulate import tabulate

def hostRangePingTab():
    reachableList, unreachableList = hostRangePing(for3task=True)
    resultDict = {}
    resultDict['Reachable'] = reachableList
    resultDict['Unreachable'] = unreachableList
    print(tabulate(resultDict, headers='keys'))