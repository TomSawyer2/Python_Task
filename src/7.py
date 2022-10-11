"""
有两个序列a，b，大小都为n，序列元素的值任意整形数，无序；
要求：通过交换a，b中的元素，使序列a元素的和与序列b元素的和之间的差最小。
"""

def getMinimumDifference(a, b):
    """
    输入：两个序列a，b，大小都为n，序列元素的值任意整形数
    输出：新的序列a，b
    :param a: list
    :param b: list
    :return: tuple
    """
    mergedList = a + b
    mergedList.sort()
    mergedListLen = len(mergedList)

    newA = []
    newB = []
    sumA = 0
    sumB = 0

    i = mergedListLen - 1
    while i >= 0:
        if sumA >= sumB:
            newB.append(mergedList[i])
            sumB = sum(newB)
        else:
            newA.append(mergedList[i])
            sumA = sum(newA)
        i -= 1

    return newA, newB

# 测试用例
a = [1, 3, 2, 5, 7]
b = [4, 10, 9, 6, 8]
print(getMinimumDifference(a, b))
