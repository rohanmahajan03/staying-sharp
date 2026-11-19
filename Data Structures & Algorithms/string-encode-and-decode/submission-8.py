class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + " " + s
        return encoded_str
            
    def decode(self, s: str) -> List[str]:
        final = []
        count = None
        count_in_progress = ""
        for i, c in enumerate(s):
            if count == None:
                if c == " ":
                    count = int(count_in_progress)
                    count_in_progress = ""
                    start_idx = i
                else:
                    count_in_progress += c
            if count is not None:
                if i - start_idx == count:
                    if count == 0:
                        final.append("")
                    else:
                        final.append(s[start_idx + 1: i + 1])
                    count = None
        return final
