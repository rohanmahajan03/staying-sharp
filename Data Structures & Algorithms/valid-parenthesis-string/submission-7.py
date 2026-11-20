class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0
        for char in s:
            if char == "(":
                left_min += 1
                left_max += 1
            elif char == ")":
                left_min -= 1 if left_min > 0 else 0
                left_max -= 1
                if left_max < 0:
                    return False
            else:
                left_min -= 1 if left_min > 0 else 0
                left_max += 1
        return True if 0 in range(left_min, left_max + 1) else False
