class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [0,3,7,2,5,8,4,6,0,1]
        # iterate through
        # if the list has a num-1 it's not start -> ignore
        # else it's a start of a sequence. 
        # -> look for num+1
        lengths = [0]
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                # Not the start of a sequence -> ignore.
                continue
            # Start of a sequence.
            count = 1
            while num+count in nums:
                count += 1
            lengths.append(count)
        return max(lengths)

        
        