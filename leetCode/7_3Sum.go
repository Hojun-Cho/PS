// 중복 처리를 안하면 set을 사용해서 answer 체크가 필요하다 ( 중복된 값이 존재하니깐)
// 전체 arr 확인보단 인덱스를 이용해서 빠르게 접근 가능한 방법으로 중복을 체크한다
func threeSum(nums []int) [][]int {
	length := len(nums)
	answer := [][]int{}
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	for i := 0; i <= length-3; i++ {
		//skip
		// 0보다 큰 이유 =>  0,0,0인 경우를 handling
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l, r := i+1, length-1
		for l < r {
			sum := nums[i] + nums[l] + nums[r]
			if sum == 0 {
				answer = append(answer, []int{nums[i], nums[l], nums[r]})
				// 정답이지만 그 안에 또 다른 정답이 존할 수 있다.
				for l < r && nums[l] == nums[l+1] {
					l += 1
				}
				for l < r && nums[r] == nums[r-1] {
					r -= 1
				}
				l++
				r--
			} else if sum > 0 {
				r--
			} else if sum < 0 {
				l++
			}
		}
	}
	return answer
}
