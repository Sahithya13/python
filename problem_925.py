class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Initialize pointers for name and typed strings
        i = j = 0
        
        # Iterate through the typed string
        while j < len(typed):
            # If the current characters match, move both pointers
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            # If the current character in typed matches the previous character in name,
            # it's a long press, so move the typed pointer
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            # If the characters don't match and it's not a long press, return False
            else:
                return False
        
        # If all characters in name have been matched, return True, else return False
        return i == len(name)
    
    """
    Approach:
    - We use two pointers, i for the name string and j for the typed string.
    - We iterate through the typed string and compare characters with the name string.
    - If the current characters match, we move both pointers.
    - If the current character in typed matches the previous character in name, it's a long press, so we move the typed pointer.
    - If the characters don't match and it's not a long press, we return False.
    - After the iteration, if all characters in name have been matched, we return True, else we return False.
    
    Time Complexity: O(n), where n is the length of the typed string.
    - We iterate through the typed string once.
    
    Space Complexity: O(1)
    - We only use a constant amount of extra space for the pointers.
    
    Best Practices:
    - Use meaningful variable names (i, j for pointers).
    - Handle edge cases (check if pointers are within bounds).
    - Provide comments explaining the approach and complexity analysis.
    - Follow a clean and readable code structure.
    """