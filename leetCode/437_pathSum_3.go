// counter를 이용해서 currSum 직전까지의 합들을 저장한다
// currSum - target에서 나온 값이 counter에 존재한다면 해당 값을 만든 노드들을 제거하고 나머지 노드들만 가지고 합을 구할 경우 target을 만들 수 있다.
// 여기서 map에 bool이 아니라 int를 사용하는 이유는  [0,1,1]이 들어가는 경우 답은 4 이지만( [0,1],[1],[0,1],[1]) bool로 계산하면 답은 2가 나온다
// 즉 같은 0 이더라도 의미하는 바가 다르다.
var answer int
var counter map[int]int

func pathSum(root *TreeNode, targetSum int) int{
	answer = 0
	counter = map[int]int{}
    counter[0]=1
	dfs_sum(root,targetSum,0)
	return answer
}

func dfs_sum(node *TreeNode, targetSum, curSum int) {
	if node == nil {
		return
	}
	curSum += node.Val
	answer += counter[curSum-targetSum]
	counter[curSum]++
	dfs_sum(node.Left,targetSum, curSum)
	dfs_sum(node.Right,targetSum, curSum)
	counter[curSum]--
	
}
