class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        n = 0
        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
                n = max(n, count_dict[i])
                continue
            count_dict[i] += 1
            n = max(n, count_dict[i])

        print(n)
        bucket = [[] for _ in range(n)]
        for key, value in count_dict.items():
            bucket[value-1].append(key)
        
        answer = []
        # print(bucket)
        for ele in reversed(bucket):
            l = len(ele)
            if k > l:
                answer.extend(ele[:])
                k-=l
            else:
                answer.extend(ele[:k])
                return answer

            

        
        
        
    
        

        