class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Edge case: If there is not enough money to distribute at least 1 dollar to each child
        if money < children:
            return -1
        
        # Calculate the maximum number of children who can receive 8 dollars
        max_eight = min(money // 8, children)
        
        # Calculate the remaining money and children after distributing 8 dollars
        remaining_money = money - (max_eight * 8)
        remaining_children = children - max_eight
        
        # Check if the remaining money can be distributed to the remaining children
        if remaining_money < remaining_children:
            return -1
        
        # Check if any child would receive 4 dollars
        if remaining_money >= remaining_children * 4:
            return -1
        
        return max_eight

    # Time Complexity: O(1)
    # The solution performs a constant number of arithmetic operations, so it runs in constant time.
    
    # Space Complexity: O(1)
    # The solution uses only a constant amount of extra space for variables, so it has constant space complexity.
    
    # Approach:
    # 1. First, we check if there is enough money to distribute at least 1 dollar to each child.
    #    If not, we return -1 since it's not possible to distribute the money.
    # 2. We calculate the maximum number of children who can receive 8 dollars by dividing the total
    #    money by 8 and taking the minimum of that value and the total number of children.
    # 3. We calculate the remaining money and children after distributing 8 dollars to the maximum
    #    number of children.
    # 4. We check if the remaining money can be distributed to the remaining children, ensuring that
    #    each child receives at least 1 dollar. If not, we return -1.
    # 5. We check if any child would receive 4 dollars by comparing the remaining money with the
    #    product of the remaining children and 4. If the remaining money is greater than or equal to
    #    this product, it means at least one child would receive 4 dollars, so we return -1.
    # 6. If all the conditions are satisfied, we return the maximum number of children who can
    #    receive 8 dollars.