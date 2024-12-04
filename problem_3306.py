class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(word)
        
        # Helper function to check if a substring contains all vowels
        def hasAllVowels(substring):
            return all(v in substring for v in vowels)
        
        # Helper function to count consonants in a substring
        def countConsonants(substring):
            return sum(c not in vowels for c in substring)
        
        count = 0
        
        # Iterate through all possible substrings
        for i in range(n):
            for j in range(i, n):
                substring = word[i:j+1]
                
                # Check if the substring has all vowels and exactly k consonants
                if hasAllVowels(substring) and countConsonants(substring) == k:
                    count += 1
        
        return count

# Time Complexity: O(n^3), where n is the length of the word
# - We have two nested loops to generate all possible substrings, which takes O(n^2) time
# - For each substring, we check if it has all vowels and count the consonants, which takes O(n) time
# - Overall, the time complexity is O(n^2 * n) = O(n^3)

# Space Complexity: O(1)
# - We only use a constant amount of extra space to store the vowels set and the count variable
# - The space used by the substring variable is proportional to the length of the word, but it is reused in each iteration
# - Therefore, the space complexity is O(1)

# Note: This solution uses a brute-force approach to generate all possible substrings and check each one.
# While it handles all edge cases and follows best coding practices, it may not be the most optimized solution
# in terms of time complexity. There might be more efficient approaches using techniques like sliding windows or
# dynamic programming to optimize the substring generation and counting process.

# Test cases:
# assert Solution().countOfSubstrings("aeioqq", 1) == 0
# assert Solution().countOfSubstrings("aeiou", 0) == 1
# assert Solution().countOfSubstrings("ieaouqqieaouqq", 1) == 3