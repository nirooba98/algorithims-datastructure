class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_hash = {}

        for i, j in enumerate(nums):
            d = target - j
            if d in my_hash:
                return[my_hash[d], i]
            my_hash[j] = i




 """ - Declare a new hashset (dictionary in Python)
     - Use enumerated 'for loop' where 'j' = value in nums array; 'i' = index of 'j'
     - Declare d = difference, check if 'd' is present in the hashset, if not add it to the hashset.
     - loop until you find 'd' and return index of 'd' and 'i' """