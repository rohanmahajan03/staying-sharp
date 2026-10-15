from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        # keep a map till length is == s1
        s1_map = Counter(s1)
        s2_map = Counter(s2[:len(s1)])
        for i in range(len(s1), len(s2)):
            print("i: ", i)
            print("s1 map: ", s1_map)
            print("s2 map: ", s2_map)
            if s1_map == s2_map:
                return True
            to_decrement = s2[i - len(s1)]
            s2_map[to_decrement] -= 1
            if s2_map[to_decrement] == 0:
                del s2_map[to_decrement]
            s2_map[s2[i]] += 1
        if s1_map == s2_map:
            return True
        return False

