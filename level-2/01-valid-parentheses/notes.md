# 🧠 Reflections & Learning – Valid Parentheses

📌 **LeetCode Link**: [https://leetcode.com/problems/valid-parentheses/description/]  
🎥 **NeetCode Video**: N/A  
✅ **My LeetCode Solution**: [https://leetcode.com/problems/valid-parentheses/submissions/2053501881/]

---

## ✅ Problem Understanding

- What is the problem asking?
We are given a string with only the brackets `()`, `[]`, `{}`. We have to check if it is valid: every opening bracket must be closed by the same type of bracket, and in the correct order.

- What are edge cases?

    - ✅ "" → Empty string (valid)
    - ✅ "(" → Only an opening bracket (invalid)
    - ✅ ")" → Closing bracket with nothing before it (invalid)
    - ✅ "([)]" → Same count of brackets but wrong order (invalid)
    - ✅ "{[]}" → Nested brackets (valid)
    - ✅ "()[]{}" → Multiple pairs side by side (valid)
    - ✅ "(((" → Many openers, no closers (invalid)

---

## 🧩 Approach

- Describe the logic in simple words.

Use a stack and a map of closing -> opening bracket.
For each character:
- If it is an opening bracket, push it on the stack.
- If it is a closing bracket, the top of the stack must be its matching opener. If the stack is empty or the top does not match, return False. Otherwise pop.
At the end, return True only if the stack is empty (no unmatched openers left).

**Time Complexity**: O(n), we visit each character once.
**Space Complexity**: O(n), in the worst case all characters are openers and sit in the stack.

---

## 💡 Key Insight

- What unlocked the solution for you?
The most recent opening bracket must be closed first (last in, first out). That is exactly how a stack works.

---

## 🚫 Mistakes / Stuck Points

- Where did you struggle?
At first I was not able to understand the question properly. Then I looked at the examples and worked through them by hand (mental math), and that is when I understood how the pattern works: the bracket opened last has to be closed first.

- What will you remember next time?
When a question is unclear, work through the given examples by hand before thinking about code. Also, always check if the stack is empty before popping, and check that the stack is empty at the end.

---