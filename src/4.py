def getOriginNum():
    """
    有一个五位数abcde，乘以4以后变成edcba，返回这个五位数
    :return: int
    """
    for i in range(10000, 100000):
        if i * 4 == int(str(i)[::-1]):
            return i
    return None

print(getOriginNum())
