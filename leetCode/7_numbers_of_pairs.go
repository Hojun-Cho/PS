func numberOfPairs(nums []int) []int {
	m, pairCount := getPairs(nums)
	last := countLast(m)

	fmt.Println(pairCount, last)
	return []int{pairCount, last}
}

func getPairs(nums []int) (map[int]int, int) {
	m := make(map[int]int, len(nums))
	answer := 0
	for _, n := range nums {
		m[n] += 1
		if m[n] == 2 {
			answer += 1
			m[n] = 0
		}
	}
	return m, answer
}

func countLast(m map[int]int) int {
	last := 0
	for k := range m {
		if m[k] != 0 {
			last += 1
		}
	}
	return last
}
