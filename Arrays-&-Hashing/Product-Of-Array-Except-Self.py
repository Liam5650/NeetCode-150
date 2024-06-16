class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        # For any position in the array, we are essentially asking ourselves
        # what is the product of everything that comes before that position (prefix) and what
        # comes after that position (postfix). First let's calculate these values

        prefix = [1] * len(nums)
        i = 0
        while i < len(nums):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]
            i += 1
        
        postfix = [1] * len(nums)
        i = len(nums) - 1
        while i >= 0:
            if i == len(nums) - 1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i + 1]
            i -= 1

        # Finally, we can calculate the product of the array discluding self, using the following
        # abstraction:
        # Nums    -> |a|b|c|d|
        # Prefix  -> |a|a*b|a*b*c|a*b*c*d|
        # Postfix -> |a*b*c*d|b*c*d|c*d|d|
        # The product at any one point is the product of the left prefix and right postfix times the value.
        # Therefore, to calculate the product without the value, it is simply done without the value added to the 
        # calculation, ie. |b*c*d|a*c*d|a*b*d|a*b*c|

        result = []
        for i in range(len(nums)):
            if i == 0:
                leftVal = 1
            else:
                leftVal = prefix[i - 1]
            if i == len(nums) - 1:
                rightVal = 1
            else:
                rightVal = postfix[i + 1]
            
            result.append(leftVal * rightVal)
        
        return result