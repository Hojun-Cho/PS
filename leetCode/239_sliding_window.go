func maxSlidingWindow(nums []int, k int) []int {
	if k == 1 {
		return nums
	}
	window := make([]int, 0)
	var push func(v int)
	// pir_queue
	push = func(v int) {
		for len(window) > 0 && v > window[len(window)-1] {
			window = window[:len(window)-1]
		}
		window = append(window, v)
	}

	answer := make([]int, 0)
	for i := 0; i < k; i++ {
		push(nums[i])
	}
	answer = append(answer, window[0])

	for i := k; i < len(nums); i++ {
		push(nums[i])
		// 윈도우의 범위에서 제거되는 값이 최댓값이라면
		if nums[i-k] == window[0] {
			window = window[1:]
		}
		answer = append(answer, window[0])
	}
	return answer
}
