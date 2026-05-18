# encoded as "{len("Hello")}#Hello"

class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string

    def extract_length(s, index) -> tuple[int, int]:
        hash_position = s.index("#", index)
        word_length = int(s[index:hash_position])
        
        index = hash_position + 1  ## Advance the index pasisng # 
        return index, word_length
            
    def decode(self, s: str) -> list[str]:
        decoded_strings = []
        index = 0
        total_length = len(s)
        
        while index < total_length:
            index, word_length = Solution.extract_length(s, index)
            
            # Extract the exact word using the length
            end_position = index + word_length
            decoded_strings.append(s[index:end_position])
            
            # Move the index to the start of the next block
            index = end_position
            
        return decoded_strings

