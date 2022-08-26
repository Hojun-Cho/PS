// hash이용
func findPairs(nums []int, k int) int {
	answer := 0
	m := map[int]int{}
	for _, n := range nums {
		m[n]++
	}

	for key := range m {
		if k == 0 {
			if m[key] > 1 {
				answer++
			}
		} else {
			if _, ok := m[key+k]; ok {
				answer++
			}
		}
	}
	return answer
}


// search를 이용
import "sort"
func findPairs(nums []int, k int) int {
	answer := 0
	length := len(nums)
	i := 0
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	for i < length {
		for i > 0 && i<length && nums[i] == nums[i-1] {
			i++
		}
		if i >= length-1 {
			break
		}

		index := sort.SearchInts(nums[i+1:], k+nums[i]) + (i + 1)
		if index < length && nums[index] == k+nums[i] {
			answer++
		}
		i++
	}
	return answer
}
