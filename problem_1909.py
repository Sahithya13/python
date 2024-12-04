class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # Initialize a variable to keep track of the number of elements removed
        removed = 0
        
        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            # Check if the current element is less than or equal to the previous element
            if nums[i] <= nums[i - 1]:
                # Increment the count of removed elements
                removed += 1
                
                # If more than one element needs to be removed, return False
                if removed > 1:
                    return False
                
                # Check if the current element is less than or equal to the element two positions back
                if i > 1 and nums[i] <= nums[i - 2]:
                    # If so, replace the current element with the previous element
                    nums[i] = nums[i - 1]
        
        # If the loop completes without returning False, the array can be made strictly increasing
        return True
    
    # Time Complexity: O(n), where n is the length of the input array nums.
    # We iterate through the array once, performing constant-time operations at each step.
    
    # Space Complexity: O(1), as we only use a constant amount of extra space to store the removed variable.
    
    # Approach:
    # 1. We initialize a variable removed to keep track of the number of elements removed.
    # 2. We iterate through the array starting from index 1.
    # 3. If the current element is less than or equal to the previous element, we increment removed.
    #    - If removed becomes greater than 1, we return False since we can't remove more than one element.
    #    - If the current element is also less than or equal to the element two positions back,
    #      we replace the current element with the previous element to maintain the strictly increasing property.
    # 4. If the loop completes without returning False, it means the array can be made strictly increasing
    #    by removing at most one element, so we return True.