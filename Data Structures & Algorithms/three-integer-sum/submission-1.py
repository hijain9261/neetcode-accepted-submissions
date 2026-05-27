class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            start = i+1
            end = len(nums)-1
            while start < end:
                second = nums[start]
                third = nums[end]
                three_sum = first + second + third
                if  three_sum == 0:
                    list_to_append = [first, second, third]
                    if list_to_append not in answer:
                        answer.append(list_to_append)
                    start+=1
                    end-=1
                elif three_sum > 0:
                    end -= 1
                else:
                    start += 1
        return(answer)

                    

















        