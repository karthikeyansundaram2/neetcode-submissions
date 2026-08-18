class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        let ans=[],i=2
        while(i>0) {
        for(let i=0;i<nums.length;i++) {
            ans.push(nums[i])
        }
         i--;
        }
        return ans;
    }
}
