"""
Given an integer array nums, return true if any value appears at least twice in the array, and return
false if every element is distinct.
"""




class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_hash = set()
        for i in nums:
            if i in my_hash:
                return True
            else:
                my_hash.add(i)


"""
- Declare a new set 'my_hash'
- Check if the integers in 'nums' array is already present in the set. Note that sets cannot have duplicate numbers.
- When the condition is false, add the integer to the set. If the condition is true, return boolean value True.
"""