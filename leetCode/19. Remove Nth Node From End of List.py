# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head 
        length = 0 
        while temp :
            temp = temp.next 
            length+=1
        # 앞에서의 index
        n = length - n 
        answer = head 
        curr = answer 
        # n == 0 이면 첫 노드를 삭제한다 
        if n == 0 : 
            return curr.next
        for i in range(n-1):
            curr = curr.next
        # 다음 노드가 None이면 curr의 노드를 삭제한다
        if curr.next == None :
            curr = None 
        # 마지막 노드를 삭제하는 경우
        elif curr.next.next == None  :
            curr.next = None
        # 사이에 있는 노드를 삭제하는 경우 
        else :
            curr.next = curr.next.next
        return answer 
        


        
