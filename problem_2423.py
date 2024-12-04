class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Create a frequency map to store the count of each character
        freq_map = {}
        for char in word:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        # Get the unique frequency counts
        freq_counts = list(freq_map.values())
        
        # If there is only one unique frequency count, removing any character will make all frequencies equal
        if len(set(freq_counts)) == 1:
            return True
        
        # If there are more than two unique frequency counts, it's impossible to equalize frequencies by removing one character
        if len(set(freq_counts)) > 2:
            return False
        
        # If there are exactly two unique frequency counts
        freq1, freq2 = set(freq_counts)
        count1, count2 = freq_counts.count(freq1), freq_counts.count(freq2)
        
        # If one frequency count occurs only once and differs by 1 from the other frequency count,
        # removing the character with that frequency will equalize frequencies
        if (count1 == 1 and freq1 - freq2 == 1) or (count2 == 1 and freq2 - freq1 == 1):
            return True
        
        # If one frequency count is 1 and occurs only once, removing that character will equalize frequencies
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
            return True
        
        return False

# Time Complexity: O(n), where n is the length of the word.
# We iterate over the word once to create the frequency map and then perform constant time operations.

# Space Complexity: O(1) since the size of the frequency map is limited by the number of lowercase English letters (26),
# which is a constant. The space used by the frequency map does not grow with the input size.

# The approach is to first create a frequency map to store the count of each character in the word.
# Then, we analyze the unique frequency counts to determine if it's possible to equalize frequencies by removing one character.

# If there is only one unique frequency count, removing any character will make all frequencies equal.
# If there are more than two unique frequency counts, it's impossible to equalize frequencies by removing one character.

# If there are exactly two unique frequency counts, we check two scenarios:
# 1. If one frequency count occurs only once and differs by 1 from the other frequency count,
#    removing the character with that frequency will equalize frequencies.
# 2. If one frequency count is 1 and occurs only once, removing that character will equalize frequencies.

# If none of the above conditions are met, it's impossible to equalize frequencies by removing one character.