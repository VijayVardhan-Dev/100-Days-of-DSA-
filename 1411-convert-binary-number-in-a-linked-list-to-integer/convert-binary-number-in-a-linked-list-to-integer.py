# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        bn = ""
        dec = 0
        cur = head
        while cur:
            val = str(cur.val)
            bn = bn + val
            cur = cur.next
        for i in range(len(bn)):
            if bn[i] != '0':
                dec = dec + int(2 ** (len(bn)-1-i))
        return dec


        