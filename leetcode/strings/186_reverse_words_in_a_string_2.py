"""186 reverse words in a string"""

class Solution:
    
    def reverse(self, start: int, end: int, words: list) -> None:
        """
        Helper function takes list, starting index and ending index.
        Reverse everyting beginning at starting index and ending at ending index. 
        """

        while start < end:
            words[start], words[end] = words[end], words[start]
            start += 1
            end -= 1

    def reverse_words(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        if n == 0:
            return s
        
        # First Step: Reverse the list
        self.reverse(0, n - 1, s)

        # Second Step: Reverse each word of input list

        start_idx = 0
        end_idx = 0

        while end_idx <= n:
            if end_idx == n or s[end_idx] == " ":
                self.reverse(start_idx, end_idx - 1, s)
                start_idx = end_idx + 1
            end_idx += 1
        
        return s
    