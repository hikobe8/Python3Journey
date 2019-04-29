# python3 数组相关的练习

# List
# 创建列表
list1 = ['Kobe', 'James', 'Rose']
list2 = [1, 2, 3, 4, 5, 6]

# 打印列表所有的内容
print("list1 = ", list1)
print("list2 = ", list2)
print("list2的长度 = ", len(list2))  # len(list) 列表的长度

# 访问列表的值
print("list1[0] = ", list1[0])
print("list2[1:3] = ", list2[1:3])

# 修改列表的值
list3 = ["Google", "MicroSoft"]  # 空列表
list3.append("Hikobe8")
print("list3原始数据 = ", list3)
del list3[1]
print("list3删除list[1] = ", list3)

# 交换列表的元素
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("list4 原始数据 = ", list4)
# 借助第三个变量
# tmp = list4[2]
# list4[2] = list4[0]
# list4[0] = tmp

# 采用和值相减
# count = list4[0] + list4[2]
# list4[0] = count - list4[0]
# list4[2] = count - list4[2]

# 位运算
# ^ 按位异或 对位相加 ，但是不进位 1 + 1 = 0 ， 1+ 0 = 1， 0 + 0 = 0

# a = list4[0]
# b = list4[2]
# a = a ^ b
# ----由上一步可知 a = a ^ b---> b = a ^ b ^b ,
# 而两个相等的数异或恒等于0,一个数与零异或恒等于自身,所有 b = a ^ 0 = a,完成了对b的赋值
# b = a ^ b
# 由上一步可知已经完成了对b的赋值, 所以 a = a ^ b = a ^ a ^ b, 上面的异或定理可知a = 0 ^ b = b,完成对a的赋值
# a = a ^ b

list4[0] = list4[0] ^ list4[2]
list4[2] = list4[0] ^ list4[2]
list4[0] = list4[0] ^ list4[2]

print("交换后的数据 = ", list4)
