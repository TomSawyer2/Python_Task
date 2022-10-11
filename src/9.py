"""
汉诺塔问题
"""

def moveOneStep(n, a, b, c):
    """
    输入：n个盘子，a柱子，b柱子，c柱子
    输出：将n个盘子从a柱子移动到c柱子的过程
    :param n: int
    :param a: str
    :param b: str
    :param c: str
    :return: None
    """ 
    if n == 1:
        print(a, '-->', c)
        return
    moveOneStep(n - 1, a, c, b)
    moveOneStep(1, a, b, c)
    moveOneStep(n - 1, b, a, c)

moveOneStep(5, 'Stack A', 'Stack B', 'Stack C')
