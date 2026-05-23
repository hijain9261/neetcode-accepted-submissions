class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: 
            return 0
        nums.sort(); i=1
        prev = nums[0]
        prev_sequence, curr_sequence = 0, 0
        while i<len(nums):
            curr = nums[i]
            if prev == curr:
                i += 1
                continue
            else:
                if curr-prev == 1:
                    print(prev, curr)
                    curr_sequence += 1
                else:
                    if prev_sequence < curr_sequence:
                        prev_sequence = curr_sequence 
                    curr_sequence = 0
                prev = curr
            i += 1  
               
        prev_sequence = max(prev_sequence, curr_sequence)+1
        return prev_sequence
                







                







        