// (n+1)/2를 하는 이유 => n=4 : [ m[0][j],m[1][j],m[2][j] ]가 필요 
// n = 3 : [ m[0][j],m[1][j] ]
// matrix를 rotate하면 회전하기 전의 행이 후의 열이 되고 행은 n-1에서 회전하기 전의 열을 뺀 결과 
func rotate(matrix [][]int) {
	n := len(matrix)

	for i := 0; i < (n+1)/2; i++ {
		for j := 0; j < n/2; j++ {
			matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] =
				matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]
		}
	}
}
