def getFactorial(x):
    """
    输入x，返回x的阶乘
    """
    n = 1
    for i in range(1, x + 1):
        n *= i
    return n

print(getFactorial(100))
