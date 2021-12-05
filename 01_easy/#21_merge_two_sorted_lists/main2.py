
# l3 = ListNode()
# prev = l3

# n1 = ListNode()
# n2 = ListNode()
# for ls1, ls2 in zip(list1, list2):
#     n1.val, n2.val = ls1, ls2
#     n1, n2 = n1.next, n2.next
# l1 = n1
# l2 = n2

# while l1 is not None and l2 is not None:
#     if l1.val <= l2.val:
#         prev.next = l1
#         l1 = l1.next
#     else:
#         prev.next = l2
#         l2 = l2.next
#     prev = prev.next

# if l1 is None:
#     prev.next = l2
# if l2 is None:
#     prev.next = l1

# return l3.next
# def MergeLists(headA, headB):
# if headA is None and headB is None:
#     return None

# if headA is None:
#     return headB
# elif headB is None:
#     return headA

# ret = ListNode()

# if headA.data < headB.data:
#     ret = headA
#     ret.next = self.mergeTwoLists(headA.next, headB)
# else:
#     ret = headB
#     ret.next = self.mergeTwoLists(headA, headB.next)

# return ret