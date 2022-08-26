// 처음 풀이 
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
  head := &ListNode{
		Val:  0,
		Next: nil,
	  }
	val := 0
	l := head
	for l1 != nil || l2 != nil {
		l1, l2, val = skip(l1, l2)
		l.Next = &ListNode{
			Val:  val,
			Next: nil,
		}
		l = l.Next
	}
	return head.Next
}

func skip(l1, l2 *ListNode) (*ListNode, *ListNode, int) {
	val := 0
	if l1 == nil {
		val = l2.Val
		l2 = l2.Next
		return l1, l2, val
	}
	if l2 == nil {
		val = l1.Val
		l1 = l1.Next
		return l1, l2, val
	}
	if l1.Val < l2.Val {
		val = l1.Val
		l1 = l1.Next
	} else {
		val = l2.Val
		l2 = l2.Next
	}
	return l1, l2, val
}

// for loop
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}
	var head *ListNode
	var cur *ListNode
	if l1.Val > l2.Val {
		head = l2
		l2 = l2.Next
	} else {
		head = l1
		l1 = l1.Next
	}

	cur = head
	for l1 != nil || l2 != nil {
		if l1 == nil {
			cur.Next = l2
			return head
		} else if l2 == nil {
			cur.Next = l1
			return head
		}

		if l1.Val < l2.Val {
			cur.Next = l1
			l1 = l1.Next
		} else {
			cur.Next = l2
			l2 = l2.Next
		}
		cur = cur.Next
	}
	return head
}

// recursion => 잘 모르겠다... 일단 참고하려고 복사
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}
	if l1.Val <= l2.Val {
		l1.Next = mergeTwoLists(l1.Next,l2)
		return l1 
	}else {
		l2.Next = mergeTwoLists(l1,l2.Next)
		return l2 
	}
}
