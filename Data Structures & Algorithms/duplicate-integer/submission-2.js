class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        
        // let map=new Map();
        // for(let i=0;i<nums.length;i++) {
        //     if(map.get(nums[i])) {
        //         return true
        //     }
        //     map.set(nums[i],1)
        // }
        // return false
        nums.sort((a,b)=> {return(a-b)})
        let i=0,j=1;
        while(j<nums.length) {
            if(nums[i]==nums[j]) {
                return true
            }
            i++;
            j++
        }
        return false

    }
}
