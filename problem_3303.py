class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)
        
        # Precompute the frequency of characters in the pattern
        pattern_freq = [0] * 26
        for char in pattern:
            pattern_freq[ord(char) - ord('a')] += 1
        
        # Initialize the frequency array for the sliding window
        window_freq = [0] * 26
        
        # Helper function to check if the current window is almost equal to the pattern
        def is_almost_equal():
            diff_count = 0
            for i in range(26):
                if window_freq[i] != pattern_freq[i]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return True
        
        # Initialize the sliding window with the first m characters of s
        for i in range(m):
            window_freq[ord(s[i]) - ord('a')] += 1
        
        # Check if the first window is almost equal to the pattern
        if is_almost_equal():
            return 0
        
        # Slide the window through s
        for i in range(m, n):
            # Remove the first character from the window
            window_freq[ord(s[i - m]) - ord('a')] -= 1
            
            # Add the new character to the window
            window_freq[ord(s[i]) - ord('a')] += 1
            
            # Check if the current window is almost equal to the pattern
            if is_almost_equal():
                return i - m + 1
        
        # No substring found that is almost equal to the pattern
        return -1
    
    """
    Approach:
    - We use the sliding window technique to find the smallest starting index of a substring in s that is almost equal to the pattern.
    - We precompute the frequency of characters in the pattern and store it in pattern_freq.
    - We initialize a sliding window of size m (length of the pattern) and compute the frequency of characters in the window using window_freq.
    - We define a helper function is_almost_equal() to check if the current window is almost equal to the pattern by comparing the frequency arrays.
    - We slide the window through s, updating the frequency array and checking if the current window is almost equal to the pattern.
    - If a substring is found that is almost equal to the pattern, we return its starting index.
    - If no such substring is found, we return -1.
    
    Time Complexity: O(n), where n is the length of s. We slide the window through s once.
    Space Complexity: O(1) since we use fixed-size arrays of size 26 to store the frequencies.
    
    Best Coding Practices:
    - Use meaningful variable names and function names for clarity.
    - Precompute the frequency of characters in the pattern to avoid redundant calculations.
    - Use a helper function to encapsulate the logic of checking if the window is almost equal to the pattern.
    - Handle edge cases properly, such as when no substring is found.
    - Provide comments to explain the approach and complexity analysis.
    """