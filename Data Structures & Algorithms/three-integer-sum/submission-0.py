class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        output=[]

        for i in range(0,len(nums)):
            if(nums[i]>0):
                break;
            if(i>0 and nums[i]==nums[i-1]):
                continue;
            
            j=i+1
            k=len(nums)-1

            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if(sum>0):
                    k-=1
                elif(sum<0):
                    j+=1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
            
        return output
        # i,j=0,len(nums)-1

        # while(i<j):
        #     sum=nums[i]+nums[j]
        #     for k in range(i+1,j):
        #         if(sum+nums[k]==0):
        #             output.append([nums[i],nums[j],nums[k]])
        #     if(sum>0):
        #         j-=1
        #     elif(sum<0):
        #         i+=1

        # return output
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if(nums[i]+nums[j]+nums[k]==0):
        #                 if([nums[i],nums[j],nums[k]] not in output):
        #                     output.append([nums[i],nums[j],nums[k]])
        
        # return output

        