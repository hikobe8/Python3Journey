import random as rd


# 单链表的反转
class Node:
    data = 0
    next = None

    def __init__(self, data):
        self.data = data


def create_list():
    head_ = Node(rd.randint(0, 100))
    current = head_
    for i in range(1, 10):
        node = Node(rd.randint(0, 100))
        current.next = node
        current = node

    return head_


def display(head_):
    current = head_
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()


# 翻转链表 - 递归方式
def reverse_list_recursion(head_):
    if head_ is None or head_.next is None:
        return head_
    re_head_ = reverse_list_recursion(head_.next)
    head_.next.next = head_
    head_.next = None
    return re_head_


# 翻转链表 - 循环方式
def reverse_list_loop(head_):
    re_head_ = head_
    current = head_
    while current is not None and current.next is not None:
        tmp: Node = current.next
        current.next = tmp.next
        tmp.next = re_head_
        re_head_ = tmp

    return re_head_


head = create_list()
print("原始数据")
display(head)
print("递归翻转:")
re_head = reverse_list_recursion(head)
display(re_head)
head = create_list()
print("原始数据")
display(head)
print("循环翻转:")
_re_head = reverse_list_loop(head)
display(_re_head)
