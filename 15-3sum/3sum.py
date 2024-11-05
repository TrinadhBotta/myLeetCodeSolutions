class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, pos, neg = set(), [], []
        z = 0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            elif nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        pos.sort()
        neg.sort()
        
        if z>2:
            ans.add((0,0,0))
        
        pos_set = set(pos)
        neg_set = set(neg)

        if z>0:

            for i in range(len(pos)):
                if -pos[i] in neg_set:
                    ans.add((0,pos[i],-pos[i]))
            
            

        for i in range(len(pos)):    
            for j in range(i+1,len(pos)):
                if -(pos[i]+pos[j]) in neg_set:
                    ans.add((pos[i],pos[j],-(pos[i]+pos[j])))  

        for i in range(len(neg)):    
            for j in range(i+1,len(neg)):
                if -(neg[i]+neg[j]) in pos_set:
                    ans.add((neg[i],neg[j],-(neg[i]+neg[j])))
        
        ans = list(ans)
        ans.sort()
        return(ans)    