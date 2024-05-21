// Converts to int does calculation and converts back.
// Doesn't work with really large numbers.

func plusOne(digits []int) []int {
    // digits = [1, 2, 3] - type []int
    sprinted := fmt.Sprint(digits) // = [1 2 3] - type string
    fielded := strings.Fields(sprinted) // = [[1 2 3]] - type []string
    joined := strings.Join(fielded, "") // = [123] - type string
    s := strings.Trim(joined, "[]") // = 123 - type string
    i, err := strconv.Atoi(s) // = 123 - type int
    if err != nil {
        // ... handle error
        panic(err)
    }
    i++ // = 124 - type int
    var array []int
    for i != 0 {
        remainder := i % 10
        array = append([]int{remainder}, array...)
        i = i / 10
    }
    return array
}