// O(n^2)
func lengthOfLongestSubstring(s string) int {
	answer := 0
	length := len(s)
	if length == 1 {
		return 1
	}
	for i := 0; i < length-1; i++ {
		last := map[byte]bool{}
		last[s[i]] = true
		for j := i + 1; j < length; j++ {
			if _, ok := last[s[j]]; ok {
				answer = max(answer, j-i)
				break
			}
			last[s[j]] = true
			if j == length-1 {
				answer = max(answer, j-i)
			}
		}
	}
	return answer
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// two pointer  O(n)
func lengthOfLongestSubstring(s string) int {
	length := len(s)
	answer := 0
	curr := 0
	used := make(map[byte]int)
	for i := 0; i < length; i++ {
        //  if used && after curr라면 curr을 갱신한다 
		if j, ok := used[s[i]]; ok && curr <= j  {
			curr = j + 1
		} else {
			answer = max(answer, i-curr+1)
		}
		used[s[i]] = i
	}
	return answer
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}rn b
}
