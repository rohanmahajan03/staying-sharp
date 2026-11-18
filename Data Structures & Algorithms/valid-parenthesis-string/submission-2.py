# 2d-dp with (i, count)

class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}
        def tryAllPaths(i, count):
            if (i, count) in cache:
                return cache[(i, count)]
            if i == len(s):
                cache[(i, count)] = True if count == 0 else False
                return cache[(i, count)]
            if s[i] == "(":
                cache[(i, count)] = tryAllPaths(i + 1, count + 1)
                return cache[(i, count)]
            elif s[i] == ")":
                if count < 0:
                    cache[(i, count)] = False
                    return cache[(i, count)]
                else:
                    cache[(i, count)] = tryAllPaths(i + 1, count - 1)
                    return cache[(i, count)]
            else:  # case when *
                if count - 1 >= 0: # means we can add a )
                    # no op, ) , (
                    cache[(i, count)] = tryAllPaths(i + 1, count) or tryAllPaths(i+1, count - 1) or tryAllPaths(i+1, count + 1)
                    return cache[(i, count)]
                else:
                    cache[(i, count)] = tryAllPaths(i + 1, count) or tryAllPaths(i + 1, count + 1)
                    return cache[(i, count)]
        return tryAllPaths(0,0)
                    

    
