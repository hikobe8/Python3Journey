import random


# 二分查找, 循环实现
def binary_search(key, arr: list):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return mid

    return -1


# 二分查找 , 递归实现
def binary_search_recursion(key, arr: list, start_, end_):
    mid_ = (start_ + end_) // 2
    if key > arr[mid_]:
        start_ = mid_ + 1
    elif key < arr[mid_]:
        end_ = mid_ - 1
    else:
        return mid_
    if start_ > end_:
        return -1
    return binary_search_recursion(key, arr, start_, end_)


def display(key, result):
    if result > -1:
        print("数据 : ", key, " 位于数组下标 ", result)
    else:
        print("数组中没有该数 : ", key)


origin_arr = list(range(0, 10
                        ))
print("原始数据 = ", origin_arr)
print("递归查找")
key1 = random.randint(0, 20)
display(key1, binary_search_recursion(key1, origin_arr, 0, len(origin_arr) - 1))
key2 = random.randint(0, 20)
display(key2,binary_search_recursion(key2, origin_arr, 0, len(origin_arr) - 1))
key3 = random.randint(0, 20)
display(key3, binary_search_recursion(key3, origin_arr, 0, len(origin_arr) - 1))
key4 = random.randint(0, 20)
display(key4, binary_search_recursion(key4, origin_arr, 0, len(origin_arr) - 1))
print("循环查找")
display(key1, binary_search(key1, origin_arr))
display(key2,binary_search(key2, origin_arr))
display(key3, binary_search(key3, origin_arr))
display(key3, binary_search(key3, origin_arr))
display(key4, binary_search(key4, origin_arr))

