class Solution:
    def trap(self, height: List[int]) -> int:
        #O(n2)
        # res = 0
       
        # for i in range(len(height)):
        #     leftmax =height[i]
        #     rightmax = height[i]
            
        #     for j in range(i):
        #         leftmax = max(leftmax,height[j])
        #     for j in range(i+1,len(height)):
        #         rightmax = max(rightmax,height[j])
        #     ans =min(leftmax,rightmax) - height[i]
        #     if ans >0:
        #         res += ans
        # return res

        #O(n)


        l, r = 0, len(height)-1
        max_l, max_r = height[l], height[r]
        res=0
        while l <r:
            if max_l<max_r:
                ans =max_l - height[l]
                if ans > 0:
                    res+= ans
                l+=1
                max_l = max(max_l , height[l])
            else:
                ans = max_r - height[r]
                if ans > 0 :
                    res+=ans
                r-=1
                max_r= max(max_r, height[r])
        return res
            