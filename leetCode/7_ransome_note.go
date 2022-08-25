func canConstruct(ransomNote string, magazine string) bool {
	rLength := len(ransomNote)
	mLength := len(magazine)
	if rLength > mLength {
		return false
	}
	if rLength == 0 && mLength == 0 {
		return true
	}
  
  // a ~ z 
	m := make([]int, 26)
	for i := 0; i < mLength; i++ {
		m[magazine[i]-'a']++
	}
	for i := 0; i < rLength; i++ {
		m[ransomNote[i]-'a']--
		if m[ransomNote[i]-'a'] < 0 {
			return false 
		}
	}
	return true
}

// split을 사용해서 추가 시간이 필요,
// arr 대신 map을 사용 
import (
    "strings"
)
func canConstruct(ransomNote string, magazine string) bool {
	length := len(ransomNote)
	m := make(map[string]int, length)
	for _, c := range strings.Split(magazine, "") {
		m[c] += 1
	}

	for _, c := range strings.Split(ransomNote, "") {
		if m[c] > 0 {
			m[c]--
			length--
		}
	}

	return length == 0
}
