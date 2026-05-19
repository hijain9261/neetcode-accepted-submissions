class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            product *= num
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero_count > 0:
                    nums[i] = 0
                else:
                    nums[i] = int(product/nums[i])
            else:
                if zero_count > 1:
                    nums[i] = 0
                else:
                    nums[i] = product
        return nums


        