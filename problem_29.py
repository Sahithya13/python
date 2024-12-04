class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle edge case: divisor is zero
        if divisor == 0:
            return 2**31 - 1
        
        # Handle edge case: dividend is -2^31 and divisor is -1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the quotient
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        
        # Convert dividend and divisor to positive values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # Initialize quotient to 0
        quotient = 0
        
        # Perform division using bit manipulation
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple
        
        # Apply the sign to the quotient
        quotient *= sign
        
        # Return the quotient
        return quotient

    # Time Complexity: O(log(dividend))
    # The while loop runs for O(log(dividend)) iterations because in each iteration,
    # the dividend is reduced by at least half of its value.
    
    # Space Complexity: O(1)
    # The solution uses only a constant amount of extra space.