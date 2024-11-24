class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # Using two moving pointers
        # Time - O(N)
        # Space - O(1)

        # word_ptr, abbr_ptr = 0, 0

        # while abbr_ptr < len(abbr):

        #     if abbr[abbr_ptr].isdigit():
        #         steps = 0

        #         if abbr[abbr_ptr] == "0":
        #             return False

        #         while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
        #             steps = steps * 10 + int(abbr[abbr_ptr])
        #             abbr_ptr += 1

        #         word_ptr += steps

        #     else:
        #         if word_ptr >= len(word):
        #             return False

        #         if word[word_ptr] != abbr[abbr_ptr]:
        #             return False

        #         word_ptr += 1
        #         abbr_ptr += 1

        # return word_ptr == len(word)


        # Re-do for the interview
        # Time - O(m + n)
        # Space - O(1)

        word_ptr, abbr_ptr = 0, 0

        while abbr_ptr < len(abbr) and word_ptr < len(word):

            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == "0":
                    return False

                skip_val = 0
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    skip_val = skip_val * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1


                word_ptr += skip_val

            else:
                if abbr[abbr_ptr] != word[word_ptr]:
                    return False

                abbr_ptr += 1
                word_ptr += 1

        return abbr_ptr == len(abbr) and word_ptr == len(word)

            