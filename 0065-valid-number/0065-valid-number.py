class Solution:
    def isNumber(self, s: str) -> bool:
        

        # Intuition


        # Starting with '-' or '+' followed by an integer/decimal.
        # Integer + optional exponent
        # Decimal + optional exponent
        # Decimal -> digits + '.' or Digits + '.' or '.' + digits + '.'
        # exponent -> 'e' or 'E' followed by an digit


        # If you see a dot then doesn't matter previous or next. 
        # If you see 'e' then you need to get a digit next
        # if sign exits, it has to be at the beginning
        # Exponent should only come after Integer or decimal.
        # Only one dot throughout
        # There should atleast be one digit.


        # You cannot find the dot after the exponent
        # You cannot find another dot; if you've found a dot before
        # You should find atleast one digit
        # You cannot find an exponent before a digit
        # You can only find digits at the very beggining or right after the exponent

        # seen_exponent, seen_dot, seen_digit

        # Solution - String manipulation
        # Time - O(n)
        # Space - O(1)

        seen_exponent = seen_dot = seen_digit = False

        for i, ch in enumerate(s):
            
            if ch in ["+", "-"]:
                if i > 0 and s[i] in ['-', '+'] and s[i - 1] not in ['e', 'E']:
                    return False
            elif ch.isdigit():
                seen_digit = True
            elif ch == ".":
                if seen_dot or seen_exponent:  # No duplicate dot and not have dot after exponent
                    return False
                seen_dot = True
            elif ch == 'e' or ch == "E":
                if not seen_digit or seen_exponent: # No duplicate exponent and have seen a digit before
                    return False
                seen_digit = False  # I have to see a digit after exponent; otherwise return False
                seen_exponent = True
            else:
                return False

        return seen_digit
