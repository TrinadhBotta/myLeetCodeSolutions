class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                carry = True
                digits[i]=0
            else:
                digits[i]+=1
                return(digits)
        digits.insert(0,1)
        return(digits)