#Time Complexity:: Average: O(n)=O(2*n)-Traversing array twice with two for loops.
#Space Complexity:: O(n) where n is the maximum number of elements.Using a new array.
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]
        for i in range(1,len(nums)):
            result.append(result[-1]*nums[i-1])
        
        suffixRunningProduct=1
        
        for i in range(len(nums)-2,-1,-1):
            result[i]=result[i]*nums[i+1]*suffixRunningProduct
            suffixRunningProduct = suffixRunningProduct* nums[i+1]
        return result