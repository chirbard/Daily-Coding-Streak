func plusOne(digits []int) []int {
    // Start from the end.
    // Add 1.
    // If the value is 9 change to 0 and add 1 to next index.
    for i := 1; i < len(digits) + 1; i++ {
        index := len(digits) - i
        fmt.Println(index)
        if index == 0 && digits[index] == 9 {
            digits[index] = 0
            digits = append([]int{1}, digits...)  // Add 1 to the front.
            break
        }
        if digits[index] == 9 {
            digits[index] = 0
            continue
        }
        digits[index] = digits[index] + 1
        break
    }
    return digits
}