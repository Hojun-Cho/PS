// 	6 ms	2.2 MB 
// strconv로 인해 느리다
func sumNumbers(root *TreeNode) int {
	return preorder(root, "")
}
func preorder(root *TreeNode, last string) int {
	rootV := strconv.Itoa(root.Val)
	now := last + rootV

	if root.Left == nil && root.Right == nil {
		n, _ := strconv.Atoi(now)
		return n
	}
	if root.Left != nil && root.Right == nil {
		return preorder(root.Left, now)
	}
	if root.Left == nil && root.Right != nil {
		return preorder(root.Right, now)
	}

	return preorder(root.Left, now) + preorder(root.Right, now)
}

// string을 이용하지 않는다
func sumNumbers(root *TreeNode) int {
	return preorder(root, 0)
}
func preorder(root *TreeNode, curr int) int {
	curr = curr*10 + root.Val
	if root.Left == nil && root.Right == nil {
		return curr
	}

	left, right := 0, 0
	if root.Left != nil {
		left = preorder(root.Left, curr)
	}
	if root.Right != nil {
		right = preorder(root.Right, curr)
	}
	return left + right
}
