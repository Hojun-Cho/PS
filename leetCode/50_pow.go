// O(n) : 2 * 2 * 2 * 2
// O(logn) : (2^2) * (2^2) =>  2 ^ 2를 한 번만 구하면 된다
func myPow(x float64, n int) float64 {
	result := invoke(x, n)
	if n < 0 {
		result = 1 / result
	}
	return result
}

func invoke(x float64, n int) float64 {
	if n == 0 {
		if x < 0 {
			return -1 
		}
		return 1
	}
	if n%2 != 0 {
		r := invoke(x, n/2)
		return x * r * r
	} else {
		r := invoke(x, n/2)
		return r * r
	}
}
