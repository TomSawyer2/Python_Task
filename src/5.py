import random
import math

def getPi():
    """
    运用Monte Carno方法计算圆周率的近似值
    :return: float
    """
    count = 0
    n = 10000000
    for _ in range(n):
        x = random.random()
        y = random.random()
        if math.sqrt(x ** 2 + y ** 2) <= 1:
            count += 1
    return 4 * count / n

print(getPi())
