class Solution(object):
    def removeElement(self, nums, val):
        
        count=0

        for i in range(len(nums)):
            if val!=nums[i]:
                nums[count] = nums[i]
                count+=1

        return count 

        
        