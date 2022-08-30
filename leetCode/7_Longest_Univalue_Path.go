var answer = 0 
func longestUnivaluePath(root *TreeNode) int {
	defer func() { answer = 0 }()
    dfs(root)
	return answer
}
func dfs(root *TreeNode) int {
	if root == nil {
		return 0
	}

	left := dfs(root.Left)
	right := dfs(root.Right)

	if root.Left != nil && root.Left.Val == root.Val {
		left++
	} else {
		left = 0
	}
	if root.Right != nil && root.Right.Val == root.Val {
		right++
	} else {
		right = 0
	}

  // 현재 노드에서는 left, right 모두 선택이 가능하다 따라서 합으로 answer을 구한다
 	answer = max(answer, left+right)
 // 현재 노드의 부모 노드는 left, right 모두 선택할 수 없다. 따라서 최댓값으로 선택한다
	return max(left, right)
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
