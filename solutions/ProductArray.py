"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Input: 'nums' = [1,2,3,4] ; Output: 'answer' = [24,12,8,6]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefix = 1
        postfix = 1
        for i in range(0, len(nums)):
            answer.append(prefix)
            prefix = prefix * nums[i]

        for j in range(len(nums)-1, -1, -1):
            answer[j] = postfix * answer[j]
            postfix = postfix * nums[j]

        return answer


"""
Input: 'nums' = [1,2,3,4] ; Output: 'answer' = [24,12,8,6]

-answer[i] should be equal to the product of the rest of the elements in the array except self.
-That means, for example, answer[1] is supposed to be product of numbers before nums[1] and product of numbers
after nums[1]. 
-Therefore, assign a value of '1' to the prefix variable. Iterate through the array from left to right and 
append the prefix values to the answer array. prefix value is updated as you iterate throughout the array 'nums'.
                        
                                prefix = prefix * nums[i]   
                                       
                                (2nd iteration: 
                                 answer[1] = 1
                                 prefix = 1 * 2 => prefix = 2)
                                 
                                (End of the iteration:
                                 answer = [1,1,2,6] )
                                 
- Do the same with a postfix and iterate through the array from right to left. Multiply the postfix values with
appended elements in the 'answer' array.

                                answer[j] = postfix * answer[j]
                                
                                (nums[3] = 4
                                 answer[3] = 1 * 6  &
                                 postfix = 1 * 4 )
                                 
                                (End of the iteration:
                                 answer = [24,12,8,6] )
                                 
- Return answer array.        
"""