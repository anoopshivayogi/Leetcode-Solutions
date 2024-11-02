class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        

        # Solution 1 - Splitting by space
        # Time - 
        # Space - 

        sentence = sentence.split(" ")

        if sentence[-1][-1] != sentence[0][0]:
            return False

        for i in range(1, len(sentence)):

            if sentence[i - 1][-1] != sentence[i][0]:
                return False


        return True  