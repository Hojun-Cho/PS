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
