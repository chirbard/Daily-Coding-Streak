function convert(s: string, numRows: number): string {
    //"PAYPALISHIRING"
    // list of strings
    // PAYP -AL- ISHI -RI- NG--
    // reverse every second one
    // PAYP -LA- ISHI -IR- NG--
    // now iterate through them ignoring -
    let list: string[] = []
    let isDiag: boolean = false
    while (s.length > 0) {
        if (!isDiag) {
            isDiag = true
            const subString: string = s.slice(0, numRows)
            s = s.substring(numRows)
            list.push(subString)
            continue
        }
        isDiag = false
        let subString: string = s.slice(0, numRows - 2)
        subString = subString.padEnd(numRows - 2, '-')
        subString = [...subString].reverse().join(""); 
        s = s.substring(numRows - 2)
        list.push(`-${subString}-`)
    }

    const listLen: number = list.length;
    list[listLen - 1] = list[listLen - 1].padEnd(numRows, '-')
    console.log(list)
    let result: string = ''
    for (let i = 0; i < numRows; i++) {
        for (let j = 0; j < listLen; j++) {
            const char: string = list[j][i]
            if (char == '-') continue
            result += char
        }
    }
    return result
};