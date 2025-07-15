class Solution:
    def isValid(self, word: str) -> bool:
        

        # Solution 1 - Straightforward
        # Time - 
        # Space - 

        if len(word) < 3:
            return False

        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_flag = False
        consonant_flag = False

        for c in word:
            if c.isalnum():
                if c.lower() in vowels:
                    vowel_flag = True
                elif not c.isdigit():
                    consonant_flag = True
            else:
                return False
        
        if vowel_flag and consonant_flag:
            return True
        else:
            return False


