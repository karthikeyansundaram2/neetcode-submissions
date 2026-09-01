class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxStore=0
        i=0
        j=len(heights)-1
        while(i<j):
            width=j-i
            height=min(heights[i],heights[j])

            maxStore=max(maxStore,height*width)

            if(heights[j]>=heights[i]):
                i+=1
            else:
                j-=1
        return maxStore

        # for i in range(0,len(heights)):
        #     for j in range(i, len(heights)):
        #         width=j-i
        #         height=min(heights[i],heights[j])

        #         maxStore=max(maxStore,height*width)
        
        # return maxStore

        