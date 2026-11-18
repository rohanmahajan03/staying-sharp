class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min_count = 0
        left_max_count = 0
        for i, char in enumerate(s):
            if char == "(":
                left_min_count += 1
                left_max_count += 1
            elif char == ")":
                if left_min_count > 0:
                    left_min_count -= 1
                if left_max_count == 0:
                    return False
                left_max_count -= 1
            else:
                if left_min_count > 0:
                    left_min_count -= 1
                left_max_count += 1
            print("curr string: ", s[:i + 1])
            print("min_count: ", left_min_count)
            print("max count: ", left_max_count)
        print("END left min count: ", left_min_count)
        print("END left max count: ", left_max_count)
        return True if 0 in range(left_min_count, left_max_count + 1) else False