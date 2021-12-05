'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, val):
        newNode = ListNode(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.val)
            current = current.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # Node for output LinkedList
        head_ptr = temp_ptr = ListNode()
        # head_ptr will be the head node of the output list
        # temp_ptr will be used to insert nodes in the output list

        # Loop for merging two lists
        # Loop terminates when both lists reaches to its end
        while list1 or list2:
            # List_1 has not reached its end and
            # List_2 has either reached its end or its current node has data
            # greater than or equal to the data of List_1 node
            # than insert List_1 node in the ouput list
            if list1 and (not list2 or list1.val <= list2.val):
                temp_ptr.next = ListNode(list1.val)
                list1 = list1.next
            # otherwise insert List_2 node in the ouput list
            else:
                temp_ptr.next = ListNode(list2.val)
                list2 = list2.next
            # move temp_pointer to next position
            temp_ptr = temp_ptr.next
        # return output list
        return head_ptr.next


# ---------------------------------------------------------- #
# Test merge() function
# Linked List with even numbers
LL1 = LinkedList()
LL1.insert(2)
LL1.insert(4)
LL1.insert(6)
LL1.insert(8)
# Linked List with odd numbers
LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(5)
LL2.insert(7)
# Merge Function
LL3 = LinkedList()
o = Solution()
LL3.head = o.mergeTwoLists(LL1.head, LL2.head)
LL3.printLL()
