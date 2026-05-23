class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True

        begin, end = 0, len(s)-1
        while begin < end:
            while begin < end and not(s[begin].isalnum()):
                begin += 1
            
            while begin < end and not(s[end].isalnum()):
                end -= 1
            
            print(s[begin], s[end])
            if s[begin].lower() != s[end].lower():
                return False
        
            begin += 1
            end -= 1
        return True



        