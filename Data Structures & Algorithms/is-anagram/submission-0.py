class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ele1, ele2 = s[i], t[i]
            if ele1 not in dict1.keys():
                dict1[ele1] = 1
            else:
                dict1[ele1] += 1
        

            if ele2 not in dict2.keys():
                dict2[ele2] = 1
            else:
                dict2[ele2] += 1
        return dict1 == dict2
        