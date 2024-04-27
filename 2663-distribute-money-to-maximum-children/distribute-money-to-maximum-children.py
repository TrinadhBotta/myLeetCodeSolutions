class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money = money-children
        if money < 0:
            return(-1)
        ans = money//7
        if ans==0:
            return(0)
        if ans > children or (ans==children and money%7!=0):
            return(children-1)
        elif ans == children-1 and money%7==3:
            return(children-2)
        return(ans)
        