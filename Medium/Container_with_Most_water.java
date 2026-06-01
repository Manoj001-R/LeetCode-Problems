class Solution {
    public int maxArea(int[] height) {

        int left =0;
        int right= height.length-1;

        int maxValue=0;
        while (left<right){
            int currentValue=Math.min(height[left],height[right]) * (right-left);
            maxValue=Math.max(maxValue,currentValue);

            if(height[left]<height[right]){
                left++;
            }else{
                right--;
            }
        }

        return maxValue;
        
    }
}