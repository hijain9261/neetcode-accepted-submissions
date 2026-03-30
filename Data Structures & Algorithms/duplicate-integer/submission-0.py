class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = {}
        for i in nums:
            if i in n.keys():
                return (True)
            else:
                n[i] = 1
        return (False)
            

