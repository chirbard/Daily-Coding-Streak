function searchInsert(nums: number[], target: number): number {
    // return index of the first value that is bigger than target.
    const len = nums.length;
    for (let i = 0; i < len; i++) {
        if (nums[i] >= target) return i;
    }
    return len;
};