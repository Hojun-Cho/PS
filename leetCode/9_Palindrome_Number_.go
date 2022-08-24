func isPalindrome(x int) bool {
	last := x
	if x < 0 {
		return false
	}
	if x < 10 {
		return true
	}
	answer := 0
	for {
		answer += x % 10
		x = x / 10
        if x == 0 {
            break 
        }
		answer *= 10
	}
	return last == answer
}
