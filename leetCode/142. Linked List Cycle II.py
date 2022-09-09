# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 토끼와 거북이
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
            if not head :
                return None
            slow=fast =head 
            while slow and fast and fast.next :
                slow = slow.next
                fast = fast.next.next
                if slow == fast :
                    # 사이클이 존재한다 하지만 위치를 모른다. 그래서 head를 따라가면서 찾는다 
                    while slow != head :
                        slow = slow.next
                        head = head.next
                    return slow
            return None
                    
            
    
