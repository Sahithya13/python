class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # Initialize variables
        max_length = 0
        left = 0
        
        # Iterate through the array
        for right in range(len(nums)):
            # Check if the current element exceeds the threshold
            if nums[right] > threshold:
                left = right + 1
                continue
            
            # Check if the current subarray is valid
            if right > 0 and nums[right] % 2 == nums[right - 1] % 2:
                left = right
            
            # Update the maximum length if necessary
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    # Time Complexity: O(n), where n is the length of the input array nums.
    # We iterate through the array once using a sliding window approach.
    
    # Space Complexity: O(1), as we only use a constant amount of extra space
    # to store variables like max_length and the pointers left and right.
    
    # Approach:
    # We use a sliding window approach to find the longest subarray that satisfies the given conditions.
    # We maintain two pointers, left and right, to define the current subarray.
    # We iterate through the array using the right pointer and check the following conditions:
    # 1. If the current element exceeds the threshold, we move the left pointer to the next element
    #    and continue to the next iteration.
    # 2. If the current subarray is invalid (i.e., the current element and the previous element have
    #    the same parity), we move the left pointer to the current position.
    # 3. We update the maximum length if necessary by taking the maximum of the current max_length
    #    and the length of the current subarray (right - left + 1).
    # Finally, we return the maximum length found.