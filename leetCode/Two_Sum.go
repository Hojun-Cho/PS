
type point struct {
	index int
	value int
}

func twoSum(nums []int, target int) []int {
	l := len(nums)
	arr := make([]point, l)
	for i, n := range nums {
		arr[i] = point{
			index: i,
			value: n,
		}
	}

	sort.Slice(arr, func(i, j int) bool {
		return arr[i].value < arr[j].value
	})

	var head = 0
	var tail = l - 1
	for head < l && tail > 0 {
		s := arr[head].value + arr[tail].value
		if s == target {
			return []int{arr[head].index, arr[tail].index}
		}
		if s > target {
			tail--
		} else {
			head++
		}
	}
	return nil
}

// hash

func twoSum(nums []int, target int) []int {
	m := make(map[int]int, len(nums))
	// value,index
	for i, n := range nums {
		m[n] = i
	}

	for i, n := range nums {
		needValue := target - n 
		if v, ok := m[needValue]; ok && v != i {
			return []int{i, v}
		}
	}
	return nil
  
  // don't need init loop
  func twoSum(nums []int, target int) []int {
    m := make(map[int]int, len(nums))
    for i, n := range nums {
      needValue := target - n 
      if v, ok := m[needValue]; ok && v != i {
        return []int{i, v}
      }
          m[n] = i
    }
    return nil
}
