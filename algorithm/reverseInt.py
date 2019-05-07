import random


# 整数反转, 未考虑整形溢出


def reverse_int(origin):
    result = 0
    while origin != 0:
        mod = origin % 10
        result = result * 10 + mod
        origin //= 10

    return result


number = random.randint(0, 100000)
print("原始数据 = ", number)
print(reverse_int(number))
