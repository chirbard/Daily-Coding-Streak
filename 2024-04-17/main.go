func lengthOfLastWord(s string) int {
    s = strings.TrimSpace(s)
    lastSpaceIndex := strings.LastIndex(s, " ")
    lastWord := s[lastSpaceIndex + 1:]
    return len(lastWord)
}