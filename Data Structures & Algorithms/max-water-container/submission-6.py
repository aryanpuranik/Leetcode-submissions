class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #O(n2) soln
        # maxx = 0
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         if min(heights[i],heights[j])* (j-i)>maxx:
        #             maxx =  min(heights[i],heights[j])* (j-i)
        # return maxx

        #More efficient soln - 2 pointer

        l =0 
        r= len(heights)-1
        max_val = 0

        while r>l:
            ans = min(heights[l],heights[r])* (r-l)
            max_val = max(max_val,ans)

            if heights[l] < heights[r]:
                l+=1
            else: r-=1
        return max_val
