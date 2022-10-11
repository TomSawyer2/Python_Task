def getPossibilities(n):
    """
    输入人数，返回至少有两个人生日相同的概率
    @param n: int
    @return: float
    """
    p = 1
    for i in range(1, n):
        p *= (365 - i + 1) / 365
    return 1 - p

print(getPossibilities(100))
