# 🧠 Reflections & Learning – Longest Substring Without Repeating Characters

📌 **LeetCode Link**: [https://leetcode.com/problems/longest-substring-without-repeating-characters/description/]  
🎥 **NeetCode Video**: N/A  
✅ **My LeetCode Solution**: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2188411236/

---

## ✅ Problem Understanding

- What is the problem asking?
  Given a string s, find the length of the longest substring (a continuous part of the string) in which no character repeats.

- What are edge cases?
  - ✅ "" → Empty string (answer 0)
  - ✅ "a" → Single character (answer 1)
  - ✅ " " → A space counts as a character (answer 1)
  - ✅ "bbbbb" → All characters same (answer 1)
  - ✅ "abcdef" → No repeats at all, whole string is valid (answer 6)
  - ✅ "abcabcbb" → Repeats start after a few characters (answer 3)
  - ✅ "pwwkew" → Answer must be a substring, not a subsequence (answer 3)
  - ✅ "dvdf" → Left pointer jumps to the middle of the window (answer 3)
  - ✅ "abba" → Old duplicate is outside the window, so left must not move backwards (answer 2)
  - ✅ "tmmzuxt" → Same idea as "abba", a stale duplicate must be ignored (answer 5)

---

## 🧩 Approach

- Describe the logic in simple words.

Use a sliding window with two pointers, `left` and `right`, and a dictionary `last_seen` that stores the last index of every character.

1. Move `right` one step at a time through the string.
2. If the current character is already in `last_seen` and its last index is inside the window (`>= left`), move `left` to one position after that index. This removes the old duplicate from the window.
3. Update `last_seen[ch] = right`.
4. The window length is `right - left + 1`. Keep the maximum in `best`.
5. Return `best`.

**Time Complexity**: O(n), `right` visits each character once and `left` never moves backwards.

**Space Complexity**: O(min(n, m)), where m is the size of the character set. The dictionary holds at most one entry per distinct character.

---

## 💡 Key Insight

- What unlocked the solution for you?
  Store the last index of each character, so when a duplicate comes I can jump `left` directly past it instead of shrinking the window one step at a time. The check `last_seen[ch] >= left` makes sure I only react to duplicates that are really inside the current window.

---

## 🚫 Mistakes / Stuck Points

- Where did you struggle?
  The sliding window logic was confusing at first. I got stuck on how `left` and `right` move together and why `left = last_seen[ch] + 1`. It became clearer when I traced small examples by hand, especially "abcbd" and "abba", step by step.

- What will you remember next time?
  Always check `last_seen[ch] >= left` before moving `left`, otherwise `left` can go backwards (example: "abba"). Also update `last_seen[ch]` on every step, not only when a duplicate is found.

---
