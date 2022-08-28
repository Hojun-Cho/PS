func majorityElement(nums []int) int {
	val, count := 0, 0

	for _, n := range nums {
		if count == 0 {
			count++
			val = n
		} else if val == n {
			count++
		} else {
			count--
		}
	}
	return val
}
