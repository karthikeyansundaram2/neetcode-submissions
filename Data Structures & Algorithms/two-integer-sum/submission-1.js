class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for(let i=0;i<nums.length;i++) {
            for(let j=i+1;j<nums.length;j++) {
                if(nums[i]+nums[j]==target) {
                    return [i,j]
                }
            }
        }
        // let i=0,j=nums.length-1;
        // nums.sort((a,b)=>{return (a-b)})
        // while(j<nums.length) {
        //     if(nums[i]+nums[j]==target){
        //         return [i,j]
        //     }
        //     if(nums[i]+nums[j]>target) {
        //         j--
        //     }
        //     else if(nums[i]+nums[j]<target){
        //         i++
        //     }
        // }
    }
}
