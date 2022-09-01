func strStr(haystack string, needle string) int {
	if haystack == needle || needle == "" {
		return 0
	}
	stackLen := len(haystack)
	needleLen := len(needle)
    for i:=0; i <= stackLen - needleLen; i ++ {
        if haystack[i:needleLen+i] == needle {
            return i 
        }
    }
    return -1 
}

func strStr(haystack string, needle string) int {
	stackLen := len(haystack)
	needleLen := len(needle)
	if stackLen < needleLen {
		return -1
	}
	if haystack == needle {
		return 0
	}
	left := 0
	for left < stackLen-needleLen +1 {
		i := 0
		start := left
		for i < needleLen && haystack[left] == needle[i] {
			i++
			left++
		}
		if left - start == needleLen {
			  return  start 
    } else {
        left = start +1 
    }
	}
	return -1 
