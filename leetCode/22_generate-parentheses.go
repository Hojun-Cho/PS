var answer []string

func generateParenthesis(n int) []string {
	current := make([]rune, n*2)
	answer = []string{}
	recursion(current, 0)
	return answer
}
func recursion(current []rune, pos int) {
	if pos == len(current) {
		if isValid(current) {
			s := string(current)
			answer = append(answer, s)
		}
		return
	}

	current[pos] = '('
	recursion(current, pos+1)
	current[pos] = ')'
	recursion(current, pos+1)
}
func isValid(current []rune) bool {
	balance := 0
	for _, c := range current {
		if c == '(' {
			balance++
		} else {
			balance--
		}
		if balance < 0 {
			return false
		}
	}
	return balance == 0
}

// 유효한 경우에만 재귀
func recursion(current []rune, pos int, open, close int) {
	if close > open {
		return
	}
	if pos == length {
		if isValid(current) {
			answer = append(answer, string(current))
			return
		} else {
			return
		}
	}

	current[pos] = '('
	recursion(current, pos+1, open+1, close)
	current[pos] = ')'
	recursion(current, pos+1, open, close+1)
}

/*
  make 주의 
  처음에 make([]string,n) 으로 주었다가 이유를 몰라서 계속 오답... 
  make([]string,n) => n = 3  : { "","",""}로 초기화 여기서 append를 하면 {"","","","("} 
*/
func generateParenthesis(n int) []string {
	a := make([]string, 0)
	if n == 0 {
		a = append(a, "")
	}

	for c := 0; c < n; c++ {
		for _, l := range generateParenthesis(c) {
			for _, r := range generateParenthesis(n - c - 1) {
				s := fmt.Sprintf("(%s)%s", l, r)
				a = append(a, s)
			}
		}
	}
	return a
}
