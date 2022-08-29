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

// map 없이
func convert(s string, numRows int) string {
    // numRows == 1 처리를 안하면 36라인에서 panic => zzLen이 0 이라서
    if numRows == 1 {
        return s
    }
    len := len(s)
	zzLen := numRows*2 - 2
	buf := strings.Builder{}
	for i := 0; i < numRows; i++ {
		temp := i
		if i == 0 || i == numRows-1 {
			for temp < len {
				buf.WriteByte(s[temp])
				temp += zzLen
			}
		} else {
			for temp < len {
				buf.WriteByte(s[temp])
				next := temp + zzLen - 2*i
				if next < len {
					buf.WriteByte(s[next])
				}
				temp += zzLen
			}
		}
	}
	return buf.String()
}
