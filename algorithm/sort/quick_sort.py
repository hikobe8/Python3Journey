# 快速排序 Python实现
import random as rd


# 递归实现快速排序
def quick_sort(un_sorted_arr, left, right):
    if left >= right or left < 0:
        return
    standard = un_sorted_arr[right]
    i = left
    j = right - 1
    while True:

        while un_sorted_arr[j] > standard:
            j -= 1
        while un_sorted_arr[i] < standard:
            i += 1

        if i < j:
            un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[j]
            un_sorted_arr[j] = un_sorted_arr[i] ^ un_sorted_arr[j]
            un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[j]
        else:
            break
    if i < right:
        un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[right]
        un_sorted_arr[right] = un_sorted_arr[i] ^ un_sorted_arr[right]
        un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[right]
    quick_sort(un_sorted_arr, left, i - 1)
    quick_sort(un_sorted_arr, i + 1, right)


# 循环实现快速排序
def quick_sort_iteration(un_sorted_arr):
    left = 0
    right = len(un_sorted_arr) - 1
    left_stack = [left]
    right_stack = [right]
    while len(left_stack) > 0 and len(right_stack) > 0:
        left = left_stack.pop()
        right = right_stack.pop()
        if left >= right:
            continue
        standard = un_sorted_arr[right]
        i = left
        j = right - 1
        while True:
            while un_sorted_arr[j] > standard:
                j -= 1
            while un_sorted_arr[i] < standard:
                i += 1
            if i < j:
                un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[j]
                un_sorted_arr[j] = un_sorted_arr[i] ^ un_sorted_arr[j]
                un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[j]
            else:
                break

        if i < right:
            un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[right]
            un_sorted_arr[right] = un_sorted_arr[i] ^ un_sorted_arr[right]
            un_sorted_arr[i] = un_sorted_arr[i] ^ un_sorted_arr[right]

        left_stack.append(left)
        right_stack.append(i - 1)
        left_stack.append(i + 1)
        right_stack.append(right)


# arr = [-100, 200, -5, 4000, 100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10000, -1232131, 2343, 0, 1, 8]
# arr = [-5,4,3,-2,2,1,0]
arr = []
for i in range(10):
    arr.append(rd.randint(-100, 100))
arr1 = arr.copy()
print("原始数组 : ", arr)
quick_sort_iteration(arr)
print("循环排序结果 : ", arr)
quick_sort(arr1, 0, len(arr1) - 1)
print("递归排序结果 : ", arr1)
