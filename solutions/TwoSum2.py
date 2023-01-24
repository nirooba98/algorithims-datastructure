class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i < j:
            Sum = numbers[i] + numbers[j]

            if Sum > target:
                j -= 1
            elif Sum < target:
                i += 1
            else:
                return [i + 1, j + 1]
            

"""
 - Initialize two pointers 'i' and  'j' to traverse through the non-decreasing integer array from the 
   beginning to the end 
   
                        numbers = [1,3,4,5,7,10,11] ; target = 9
                                   |             |
                                   i             j
                                   
 - While the left pointer is smaller than the right pointer, add the sum of the respective two integers
 - Check if the sum of two numbers is greater or smaller or exactly equal to the target integer. 
 - If the sum is greater, decrement the value of j by 1 and add the sum again.
 
                        numbers = [1,3,4,5,7,10,11] 
                                   |          |
                                   i          j
                                   
 - If the sum is smaller, increment the value of i by 1 and add the sum again
 
                        numbers = [1,3,4,5,7,10,11] 
                                     |     |
                                     i     j
                                   
 - If the sum is equal, return the integer's indices + 1, i.e., [i+1, j+1]
 
                        numbers = [1,3,4,5,7,10,11] 
                                       | |
                                       i j                                                
"""