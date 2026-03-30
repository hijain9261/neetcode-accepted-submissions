class Solution:
    def criteria(word1, word2):
        if len(word1) != len(word2):
            return False

        w1 = list(word1)
        w2 = list(word2)

        for char in w1:
            if char not in w2:
                return False
            w2.remove(char)

        return True

    def check_amalgam(word1, list_of_amalgams):
        for i in range(len(list_of_amalgams)):
            if Solution.criteria(word1, list_of_amalgams[i][0]):
                return i, True
        return -1, False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_of_amalgams = []
        for word in strs:
            index, found = Solution.check_amalgam(word, list_of_amalgams)
            if found:
                list_of_amalgams[index].append(word)
            else:
                list_of_amalgams.append([word])
        return list_of_amalgams





        