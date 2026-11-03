from typing import Dict, List


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        # map each closing bracket to its matching opening bracket
        dt: Dict[str, str] = {"}": "{", ")": "(", "]": "["}

        for ch in s:
            if ch in dt:
                # closing bracket: top of stack must be its matching opener
                if stack and stack[-1] == dt[ch]:
                    stack.pop()
                else:
                    return False
            else:
                # Opening bracket: remember it
                stack.append(ch)

        # valid only if no unmatched opening brackets are left
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("{[]}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("") is True
    assert sol.isValid("(") is False
    assert sol.isValid(")") is False

    print("all test cases passed!")