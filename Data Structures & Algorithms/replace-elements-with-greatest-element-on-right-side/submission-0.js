class Solution {
    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {

       let max=arr[arr.length-1]
       arr[arr.length-1]=-1
       let j=arr.length-2
       while(j>=0){
        if(max>arr[j]) {
            arr[j]=max
        }
        else if(arr[j]>max) {
            let t=arr[j]
            arr[j]=max
            max=t
        }
        j--;
       }
       return arr;
    }
}
