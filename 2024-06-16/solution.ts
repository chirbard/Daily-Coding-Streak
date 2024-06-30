// I think i should solve this using two pointers.
// One pointer always moves.
// The other only moves when right pointer is not on a duplicate.


function removeDuplicates(nums: number[]): number {
    let leftPointer: number = 1;
    let rightPointer: number = 1;
    let k: number = 1;
    const length: number = nums.length;
    let last: number = nums[0];
    while (rightPointer < nums.length) {
        if (nums[rightPointer] == last) {
            console.log('duplicate')
            // --- duplicate ----
            // don't add to k
            // move only right pointer
            last = nums[rightPointer];
            rightPointer++;
            continue
        }
        last = nums[rightPointer];
        nums[leftPointer] = nums[rightPointer]
        k++;
        leftPointer++;
        rightPointer++;
    }
    console.log(nums)
    return k;
};