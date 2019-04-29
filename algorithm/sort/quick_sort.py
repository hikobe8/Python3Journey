# 快速排序 Python实现


# 递归实现快速排序
def quick_sort(un_sorted_arr, left, right):
    o_l = left
    o_r = right
    if left >= right or left < 0:
        return
    sIndex = right
    standard = un_sorted_arr[sIndex]
    right = o_r - 1
    while True:

        while un_sorted_arr[right] > standard:
            right -= 1
        while un_sorted_arr[left] < standard:
            left += 1

        if left < right:
            un_sorted_arr[left] = un_sorted_arr[left] ^ un_sorted_arr[right]
            un_sorted_arr[right] = un_sorted_arr[left] ^ un_sorted_arr[right]
            un_sorted_arr[left] = un_sorted_arr[left] ^ un_sorted_arr[right]
        else:
            break
    if left < sIndex:
        un_sorted_arr[left] = un_sorted_arr[left] ^ un_sorted_arr[sIndex]
        un_sorted_arr[sIndex] = un_sorted_arr[left] ^ un_sorted_arr[sIndex]
        un_sorted_arr[left] = un_sorted_arr[left] ^ un_sorted_arr[sIndex]
    quick_sort(un_sorted_arr, o_l, left - 1)
    quick_sort(un_sorted_arr, left + 1, o_r)


arr = [-100, 200, -5, 4000, 100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10000, -1232131, 2343, 0, 1, 8]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
