class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        lmin,lmax=[(nums[0],0)], [(nums[0],0)]

        rmax,rmin=[0]*n, [0]*n
        rmax[-1]=(nums[-1],n-1)
        rmin[-1]=(nums[-1],n-1)

        for i in range(1,n):
            lmn = lmin[-1][0]
            lmx = lmax[-1][0]

            rmn = rmin[n-i][0]
            rmx =  rmax[n-i][0]

            if lmn>nums[i]:
                lmin.append((nums[i],i))
            else:
                lmin.append(lmin[-1])
            
            if lmx<nums[i]:
                lmax.append((nums[i],i))
            else:
                lmax.append(lmax[-1])

            if rmn>nums[n-1-i]:
                rmin[n-1-i]=(nums[n-1-i],n-i-1)
            else:
                rmin[n-1-i]=rmin[n-i]
            
            if rmx<nums[n-1-i]:
                rmax[n-1-i]=(nums[n-1-i],n-i-1)
            else:
                rmax[n-1-i]=rmax[n-i]
        
        for i in range(n):
            x= i+indexDifference
            if x>=n:
                return([-1,-1])
            if rmax[x][0]-lmin[i][0]>=valueDifference:
                return([lmin[i][1],rmax[x][1]])
            
            if lmax[i][0]-rmin[x][0]>=valueDifference:
                return([lmax[i][1],rmin[x][1]])
        return([-1,-1])