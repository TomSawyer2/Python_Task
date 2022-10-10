def getJumpCounts(n):
    """
    输入台阶数，返回跳法数
    只用最近两个台阶的跳法数，空间复杂度O(1)
    """
    a, b = 1, 1

    for _ in range(n):
        a, b = b, a + b
    return a

print(getJumpCounts(100))
