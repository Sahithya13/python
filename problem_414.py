class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Initialize three variables to keep track of the top three distinct maximum numbers
        max1 = max2 = max3 = float('-inf')
        
        # Iterate through the array
        for num in nums:
            # Skip duplicates
            if num in [max1, max2, max3]:
                continue
            
            # Update max1, max2, and max3 accordingly
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
        
        # If the third maximum exists, return it; otherwise, return the maximum number
        return max3 if max3 != float('-inf') else max1

# Time Complexity: O(n), where n is the length of the input array nums.
# We iterate through the array once, performing constant-time operations for each element.

# Space Complexity: O(1) since we only use a constant amount of extra space to store max1, max2, and max3.

# Approach:
# 1. Initialize three variables (max1, max2, max3) to keep track of the top three distinct maximum numbers.
#    Set them to negative infinity initially to handle cases where the array contains negative numbers.
# 2. Iterate through the array:
#    - Skip duplicates by checking if the current number is already equal to max1, max2, or max3.
#    - If the current number is greater than max1, update max3, max2, and max1 accordingly.
#    - If the current number is greater than max2, update max3 and max2 accordingly.
#    - If the current number is greater than max3, update max3 accordingly.
# 3. After the iteration, if max3 is not equal to negative infinity, it means the third maximum exists, so return max3.
#    Otherwise, return max1, which represents the maximum number in the array.

# The solution handles edge cases such as:
# - Arrays with fewer than three distinct numbers
# - Arrays containing duplicate numbers
# - Arrays with negative numbers

# The solution is optimized for time and space complexity, avoiding the need for sorting or extra data structures.
# It follows best coding practices with clear variable names and comments explaining the approach and complexity analysis.