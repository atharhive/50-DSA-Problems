from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # stores the most recent index where each character was seen
        last_seen: Dict[str, int] = {}
        left = 0   # left edge of the current window
        best = 0   # length of the longest valid window so far

        for right, ch in enumerate(s):
            # if ch is already inside the current window, move left past
            # its previous position so the window has no duplicates again
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring(" ") == 1
    assert sol.lengthOfLongestSubstring("a") == 1
    assert sol.lengthOfLongestSubstring("abba") == 2  # left must never move backwards
    assert sol.lengthOfLongestSubstring("dvdf") == 3
    assert sol.lengthOfLongestSubstring("tmmzuxt") == 5

    print("All test cases passed!")