class LongestSubstringLengthSolution:
    """A class for containing different implementations of an algorithm
    that finds the longest substring for a given string
    """
    
    def __init__(self, implementation="sliding_window"):
        self.implementation = implementation

    @staticmethod
    def sliding_window(s: str) -> int:
        """Return the longest continuous substring of the input string

        Args:
            s (str): The input string

        Returns:
            int: The number of characters in the longest continuous substring
        """
        char_index = {}
        longest = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            char_index[char] = end
            longest = max(longest, end - start + 1)

        return longest
    
    def longest_substring(self, s: str) -> int:
        if self.implementation == "sliding_window":
            return self.sliding_window(s)