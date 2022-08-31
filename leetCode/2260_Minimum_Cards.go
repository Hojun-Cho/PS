func minimumCardPickup(cards []int) int {
	have := map[int]int{}
	limit := 99999999
	answer := limit
	for i, card := range cards {
		if j, ok := have[card]; ok {
			answer = min(answer, i-j+1)
		}
		have[card] = i
	}
	if answer == limit {
		return -1 
	}
	return answer 
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
