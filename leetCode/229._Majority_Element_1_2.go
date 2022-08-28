// 169. Majority Element
// 최대 1
func majorityElement(nums []int) int {
	val, count := 0, 0

	for _, n := range nums {
		if count == 0 {
			count++
			val = n
		} else if val == n {
			count++
		} else {
			count--
		}
	}
	return val
}

// 229. Majority Element II
// 최대 2
func majorityElement(nums []int) []int {
    count1,count2,val1,val2 := 0,0,0,1 
    limit := len(nums)/3
    for _,n := range nums{
        if val1 == n {
            count1++
        }else if val2 == n {
            count2++
        }else if count1 == 0{
            val1 = n 
            count1++
        }else if count2 == 0 {
            val2 = n 
            count2++
        }else {
            // complete pair
            count1--
            count2--
        }
    }
    
    c1,c2 := 0 , 0
    for _,n := range nums{
        if n == val1 {
            c1++
        }    
        if n == val2 {
            c2 ++
        }
    }
 
    answer := []int{}
    if c1 > limit {
        answer = append(answer,val1)
    }
    if c2 > limit{
        answer = append(answer,val2)
    }
    return answer 
}
