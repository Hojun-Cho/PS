// Add Two Numbers
// 처음에 strings.join을 이용 => int 범위를 초과하는 값이 있음 따라서 join을 이용한 풀이는 불가능

import (
	"strings"
    "fmt"
)

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	head := &ListNode{}
	cur := head
	for l1 != nil || l2 != nil || carry != 0 {
		n1, n2 := 0, 0
		if l1 != nil {
			n1 = l1.Val
            l1 = l1.Next
		}
		if l2 != nil {
			n2 = l2.Val
            l2 = l2.Next
		}
		n := n1 + n2 + carry
		carry = n / 10
        
		cur.Next = &ListNode{
			Val:  n % 10,
			Next: nil,
		}
		cur = cur.Next
	}
	return head.Next
}
