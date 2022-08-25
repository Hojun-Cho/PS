func isValid(s string) bool {
	open := map[rune]rune{
		'(': ')',
		'[': ']',
		'{': '}',
	}
	close := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}
	arr := make([]rune, 0)
	for _, c := range s {
		if _, ok := open[c]; ok {
			arr = append(arr, c)
		} else if length := len(arr); length <= 0 {
			return false
		} else {
			if close[c] == arr[length-1] {
				arr = arr[:length-1]
			} else {
				return false
			}
		}
	}
	return len(arr) == 0
}
