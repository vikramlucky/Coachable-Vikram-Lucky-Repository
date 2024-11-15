"""49. Group Anagrams"""

from collections import defaultdict
from typing import List

class Solution:
    """Solution Class"""

    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        This function groups anagrams by counting the respective characters by their ASCII ordering
        in an array. Then, serializing them into tuples so that it's hashable. Thus, any string
        that serializes to an existing encoding will be added to that collection. Finally, we
        return the groupings to the caller.
        """

        anagrams_map = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                char_count[index] += 1
            key = tuple(char_count)

            anagrams_map[key].append(word)

        return list(anagrams_map.values())
