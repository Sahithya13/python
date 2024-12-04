class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        # Iterate through all possible substrings
        for i in range(n):
            zeros = 0
            ones = 0
            
            # Count the number of zeros and ones in each substring
            for j in range(i, n):
                if s[j] == '0':
                    zeros += 1
                else:
                    ones += 1
                
                # Check if the substring has dominant ones
                if ones >= zeros ** 2:
                    count += 1
        
        return count
    
    # Time Complexity: O(n^2), where n is the length of the string s
    # Space Complexity: O(1), as we only use a constant amount of extra space
    
    # Approach:
    # 1. We iterate through all possible substrings of s using two nested loops.
    # 2. For each substring, we count the number of zeros and ones.
    # 3. If the number of ones is greater than or equal to the square of the number of zeros,
    #    we increment the count of substrings with dominant ones.
    # 4. Finally, we return the total count of substrings with dominant ones.
    
    # Note: This solution uses a brute-force approach and has a time complexity of O(n^2).
    # For larger inputs, a more optimized solution using dynamic programming or other techniques
    # may be required to improve the time complexity.