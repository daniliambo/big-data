# !/usr/bin/python
import sys

counter = 0
prices = []
for line in sys.stdin:
    if counter == 0:
        counter += 1
        continue
    if len(prices) == 5000:
        mean = sum(prices) / len(prices)
        var = 1 / len(prices) * sum([(p - mean) ** 2 for p in prices])
        cz = len(prices)
        print('%s\t%s\t%s\n' % (cz, mean, var), end='')
        prices = []

    try:
        price = int(line.rstrip().split(',')[-7])
        prices.append(price)
    except IndexError:
        pass

if len(prices) != 0:
    mean = sum(prices) / len(prices)
    var = 1 / len(prices) * sum([(p - mean) ** 2 for p in prices])
    cz = len(prices)
    print('%s\t%s\t%s\n' % (cz, mean, var), end='')
    prices = []

# - Интерпретировать каждую строчку как чанк из одного элемента и отправлять редюсеру значения вида (1, x, 0)
# - Агрегировать данные за k строчек и отправлять одно значение вида (ck, mk, vk)
