from task1 import hostPing
from task2 import hostRangePing
from task3 import hostRangePingTab

# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов. 
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом. 
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address(). 
# (Внимание! Аргументом сабпроцеса должен быть список, а не строка!!! Крайне желательно использование потоков.)
# 2. Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1) для перебора ip-адресов из заданного диапазона. 
# Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
# 3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. 
# Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате 
# (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
# Reachable

# 10.0.0.1
# 10.0.0.2
# Unreachable

# 10.0.0.3
# 10.0.0.4

testList = ['127.0.0.1', 'aaa', 'gb.ru', 'google.com', '1.2.3.4'] # for first task test

flag = int(input('Input number of task you want to test (1, 2 or 3): '))
if flag == 1:
    hostPing(testList)
elif flag == 2:
    hostRangePing()
elif flag == 3:
    hostRangePingTab()
