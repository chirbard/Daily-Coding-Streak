function strStr(haystack: string, needle: string): number {
    // Compare needle to haystack substring of same length.
    // If they don't match then pop the first char of haystack.
    // If haystack is shorter than needle then return -1.
    var index: number = 0;
    const len: number = needle.length;
    while (haystack.length >= len) {
        const subString: string = haystack.slice(0, len);
        if (subString == needle) return index;
        haystack = haystack.substring(1);
        index++;
    }
    return -1;
};