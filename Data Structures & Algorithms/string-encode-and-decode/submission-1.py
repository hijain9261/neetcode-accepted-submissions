class Solution:
    def encode(self, strs) -> str:
        encoded_string = ""
        for words in strs:
            encoded_string += str(len(words)) + "#" +words
        return encoded_string

    def extract (s, i) -> int:
        after_i_hash = s.index("#", i)
        value = int(s[i: after_i_hash])
        i = i + len(str(value))
        return i, value
            
    def decode(self, s: str) -> str:
        strs = []
        i = 0; l = len(s)
        while i < l:
            i, k = Solution.extract(s, i)
            strs.append(s[i+1: i+1+k:])
            i = i + k + 1
        return (strs)


