"""
一普查员问一位女士，“你有多少个孩子，他们多少岁？”
女士回答：“我有三个孩子，他们的岁数相乘是36，岁数相加就等于隔离间屋的门牌号码。”
普查员立刻走到隔邻，看了一看，回来说：“我还需要多少资料。”
女士回答：“我现在很忙，我最大的孩子正在楼上睡觉。”
普查员说：“谢谢，我己知道了。”
返回三个孩子的岁数

条件1：三个孩子的岁数相乘是36
条件2：三个孩子的岁数相加的结果在条件1中有重复解
条件3：三个孩子中有一个年纪最大
"""

originAgeList = list(range(1, 37))

ageList = []  # 所有年龄的组合

def getAgeList(x, y, z):
    """
    按条件1筛选组合，返回结果
    :param x: int
    :param y: int
    :param z: int
    :return: list
    """
    # 条件1：三个孩子的岁数相乘是36 -> 获取所有x * y * z = 36的组合
    temp = []
    if x * y * z == 36:
        temp.append(x)
        temp.append(y)
        temp.append(z)
        # 去重
        temp.sort()
        if temp not in ageList:
            ageList.append(temp)

def getSum():
    """
    按条件2和3筛选组合，返回结果
    :return: list
    """
    # 条件2：三个孩子的岁数相加的结果在条件1中有重复解
    tempList = []
    for temp in ageList:
        tempList.append(sum(temp))
    # 获取年龄和重复的组合
    for a in tempList:
        findCount = tempList.count(a)
        if findCount > 1:
            tempList.remove(a)
            for item in ageList:
                if sum(item) == a:
                    # 条件3： 三个孩子中有一个年纪最大
                    if item.count(max(item)) == 1:
                        return item

def getChildsInfo():
    """
    按条件顺序筛选组合，返回结果
    :return: list
    """
    for p1 in originAgeList:
        for p2 in originAgeList:
            for p3 in originAgeList:
                getAgeList(p1, p2, p3)
                list = getSum()
                if list:
                   return list

print(getChildsInfo())
