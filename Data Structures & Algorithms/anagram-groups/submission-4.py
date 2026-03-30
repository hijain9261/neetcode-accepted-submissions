class Solution:
    def criteria(word1, word2):
        word1 = list(word1)
        word2 = list(word2)
        if len(word1) == len(word2):
            while (len(word1) != 0):
                char = word1.pop()
                if char not in word2:
                    return False
                else:
                    word2.remove(char)
            return True 


    def check_amalgam(word1, list_of_amalgams):
        word2 = ""
        for i in range(len(list_of_amalgams)):
            word2 = list_of_amalgams[i][0]
            if Solution.criteria(word1, word2):
                return i, True
        return -1, False
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_amalgams = []
        for word in strs:
            index, Cond = Solution.check_amalgam(word, list_of_amalgams)
            if Cond:
                list_of_amalgams[index].append(word)
            else:
                list_of_amalgams.append([word])
        return (list_of_amalgams)






        