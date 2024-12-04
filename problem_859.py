class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Check if lengths of s and goal are equal
        if len(s) != len(goal):
            return False
        
        # Check if s and goal are already equal
        if s == goal:
            # If s and goal are equal, check if there are any duplicate characters in s
            return len(set(s)) < len(s)
        
        # Find the indices where s and goal differ
        diff_indices = [i for i in range(len(s)) if s[i] != goal[i]]
        
        # If there are exactly 2 differences and the characters at those indices are swapped in s and goal
        return len(diff_indices) == 2 and s[diff_indices[0]] == goal[diff_indices[1]] and s[diff_indices[1]] == goal[diff_indices[0]]
    
    # Time Complexity: O(n), where n is the length of the input strings s and goal.
    # We iterate through the strings once to find the differing indices.
    
    # Space Complexity: O(n) in the worst case, where all characters in s and goal differ.
    # In the worst case, we store all the differing indices in the diff_indices list.
    
    # The solution handles the following cases:
    # 1. If the lengths of s and goal are not equal, it returns False since swapping characters won't make them equal.
    # 2. If s and goal are already equal, it checks if there are any duplicate characters in s. If there are, it returns True since swapping two same characters will still result in the same string.
    # 3. If there are exactly two differences between s and goal, it checks if swapping the characters at those indices in s will make it equal to goal.
    
    # The solution is optimized for time and space complexity, follows best coding practices with clear variable names and comments, and includes complexity analysis.
    
    # Example test cases:
    # assert buddyStrings("ab", "ba") == True
    # assert buddyStrings("ab", "ab") == False
    # assert buddyStrings("aa", "aa") == True
    # assert buddyStrings("aaaaaaabc", "aaaaaaacb") == True
    # assert buddyStrings("", "aa") == False