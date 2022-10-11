"""
八皇后问题
"""

def judgeConflict(state, nextColumn):
    """
    判断目前棋盘上的状态是否符合题意
    @param state: tuple 每一行中皇后所在的位置
    @param nextColumn: int 下一行的列坐标
    @return: boolean
    """
    nextRow = rows = len(state)
    for row in range(rows):
        column = state[row]
        # 只需判断是否在同一行或者是否在对角线
        if abs(column - nextColumn) in [0, nextRow - row]:
            return True
    return False

def queens(num, state = ()):
    """
    回溯算法计算每一种结果
    @param num: int 皇后的数量
    @param state: int 列坐标
    @return: None
    """
    for pos in range(num):
        if not judgeConflict(state, pos):
            stateLength = len(state)
            if stateLength == num - 1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos, )):
                    # 递归调用
                    yield (pos, ) + result

def printInFormat(solution):
    """
    格式化显示棋盘
    @param solution: tuple 结果
    @return: None
    """
    def line(pos, length = len(solution)):
        return '·' * (pos) + 'X' + '·' * (length - pos - 1)

    for pos in solution:
        print(line(pos))

solutions = queens(8)
for index, solution in enumerate(solutions):
    print((index + 1), solution)
    printInFormat(solution)
    print('\n')
