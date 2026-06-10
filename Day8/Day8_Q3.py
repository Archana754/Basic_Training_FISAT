#https://leetcode.com/problems/middle-of-the-linked-list/
#BRUTE FORCE



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt=0
        temp=head
        while temp:
            cnt+=1
            temp=temp.next
        mid=cnt//2
        temp2=head
        for i in range(mid):
            temp2=temp2.next
        return temp2



