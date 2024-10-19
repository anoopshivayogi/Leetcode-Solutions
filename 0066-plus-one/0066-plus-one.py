class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        carry = 0

        for idx in range(len(digits) - 1, -1, -1):

            cur_num = carry + digits[idx]

            if not res:
                cur_num += 1
            
            carry = cur_num // 10
            cur_num = cur_num % 10

            res.append(cur_num)

        if carry:
            res.append(carry)

        return res[::-1]

        

                
            
                
