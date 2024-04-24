func singleNumber(nums []int) int {
    // create hashmap
    // if value in hashset then pop value
    // the value that stays in the hashset is the answer
    m := make(map[int]int)

    for i := 0; i < len(nums); i++ {
        value := nums[i]
        _, keyExists := m[value]
        if keyExists {
            delete(m, value)
            continue
        }
        m[value] = 1
    }
    answer := 0
    for key, _ := range m {
        answer = key
    }
    return answer
}