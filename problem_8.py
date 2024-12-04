class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize variables
        result = 0
        sign = 1
        i = 0
        n = len(s)
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Determine the sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = 1 if s[i] == '+' else -1
            i += 1
        
        # Step 3: Read the integer
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Apply the sign to the result
        result *= sign
        
        # Step 4: Round the integer if out of range
        result = max(min(result, 2**31 - 1), -2**31)
        
        return result
    
    # Time Complexity: O(n), where n is the length of the input string s.
    # We iterate through the string once to process each character.
    
    # Space Complexity: O(1), as we only use a constant amount of extra space
    # to store variables, regardless of the input size.
    
    # The solution follows these steps:
    # 1. Initialize variables to store the result, sign, and index.
    # 2. Ignore leading whitespace by incrementing the index until a non-whitespace character is found.
    # 3. Determine the sign by checking if the current character is '+' or '-'.
    # 4. Read the integer by iterating through the string and converting each digit to an integer.
    #    We stop when a non-digit character is encountered or the end of the string is reached.
    # 5. Apply the sign to the result.
    # 6. Round the integer if it is out of the 32-bit signed integer range.
    # 7. Return the final result.
    
    # The solution handles edge cases such as:
    # - Leading whitespace
    # - Positive or negative sign
    # - Reading only valid digits
    # - Rounding the integer if it is out of range
    # - Returning 0 if no valid integer is found
    
    # The code follows best practices such as:
    # - Using meaningful variable names
    # - Adding comments to explain the logic and complexity
    # - Handling edge cases and constraints
    # - Optimizing for time and space complexity