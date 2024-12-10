class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        # Solution 1 - Straightforward solution
        # Time - O(n) - where n is the number of characters in the sentence
        # Space - O(n) - result string has n chars

        words = sentence.split()
        res = []

        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for idx, word in enumerate(words):
            cur_word = ''

            if word[0].lower() in vowels:
                cur_word += word
            else:
                cur_word += word[1:] + word[0]

            cur_word += 'ma'

            cur_word += ('a' * (idx + 1))

            res.append(cur_word)

        return ' '.join(res)
