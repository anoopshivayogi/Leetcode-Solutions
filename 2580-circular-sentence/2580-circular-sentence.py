class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        

        # Solution 1 - Splitting by space
        # Time - O(n)
        # Space - O(n)

        # sentence = sentence.split(" ")

        # if sentence[-1][-1] != sentence[0][0]:
        #     return False

        # for i in range(1, len(sentence)):

        #     if sentence[i - 1][-1] != sentence[i][0]:
        #         return False

        # return True


        # Solution 2 - Space optimised approach without splitting
        # Time - O(n)
        # Space - O(1)


        for idx in range(len(sentence)):

            if sentence[idx] == " ":
                if sentence[idx - 1] != sentence[idx + 1]:
                    return False

                
        return sentence[0] == sentence[-1]