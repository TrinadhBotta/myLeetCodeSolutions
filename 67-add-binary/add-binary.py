class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        s = ''
        a = a[::-1]
        b = b[::-1]
        m = len(a)
        n = len(b)
        if m>n:
            x = ''.join('0' for i in range(m-n))
            b+=x
        else:
            x = ''.join('0' for i in range(n-m))
            a+=x
        ans = ''
        carry = 0
        for i in range(len(a)):
            summ = int(a[i])+int(b[i])+carry
            if summ==2:
                ans+='0'
                carry = 1
            elif summ == 3:
                ans+='1'
                carry = 1
            elif summ == 1:
                ans+='1'
                carry = 0
            else:
                ans+='0'
                carry =0
        if carry == 1:
            ans+='1'
        return(ans[::-1])