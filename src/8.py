"""
有三顶红帽子和两顶白帽子。
将其中的三顶帽子分别戴在 A、B、C三人头上。
这三人每人都只能看见其他两人头上的帽子，但看不见自己头上戴的帽子，并且也不知道剩余的两顶帽子的颜色。
问A：“你戴的是什么颜色的帽子？” A回答说：“不知道。” 
接着，又以同样的问题问B。B想了想之后，也回答说：“不知道。” 
最后问C。C回答说：“我知道我戴的帽子是什么颜色了。” 
当然，C是在听了A、B的回答之后而作出回答的。
请尝试用编程方法解答此问题。
"""

possibleList = []

def getPossibleList():
  """
  枚举所有情况
  """
  # 0-红帽子 1-白帽子
  for a in range(2):
      for b in range(2):
          for c in range(2):
            possibleList.append([a, b, c])

def getAnswer():
  """
  筛选枚举得到的结果，返回答案
  :return: list
  """
  getPossibleList()
  # A不知道自己帽子的颜色 -> B和C不可能都是白色帽子
  possibleList[:] = [x for x in possibleList if x[1] != x[2] or (x[1] == x[2] and x[1] == 0)]

  # B不知道自己帽子的颜色 -> A和C不可能都是白色帽子
  possibleList[:] = [x for x in possibleList if x[0] != x[2] or (x[0] == x[2] and x[0] == 0)]

  # C知道自己帽子的颜色 -> A和B不可能都是白色帽子
  possibleList[:] = [x for x in possibleList if x[0] != x[1] or (x[0] == x[1] and x[0] == 0)]
  # 同时易得A和B都不可能带白帽子，否则AB中任何一人都可以判断
  possibleList[:] = [x for x in possibleList if x[0] != 1 and x[1] != 1]
  # 此外，C也不可能带白帽子，否则C可以判断
  possibleList[:] = [x for x in possibleList if x[2] != 1]

  return possibleList

print(getAnswer()[0].__str__() + "（0-红帽子 1-白帽子）")
