// map을 이용한 풀이 
func convert(s string, numRows int) string {
	m := map[int][]byte{}
	i := 0
	len := len(s)
	for i < len {
		for j := 0; j < numRows && i < len; j++ {
			m[j] = append(m[j], s[i])
			i++
		}
		for j:= numRows-2 ; j>= 1 && i < len;j-- {
			m[j] = append(m[j], s[i])
			i++
		}
	}
	builder := strings.Builder{}
	for i := 0; i < numRows; i++ {
		builder.Write(m[i])
	}
	return builder.String()
}
