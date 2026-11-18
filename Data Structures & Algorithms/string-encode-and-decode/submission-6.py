class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "@" + s
        print("encoded string: ", res)
        return res
            
    "5hello5world"
    "0"

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        str_list = []
        count = None
        count_str = ""
        start_idx = 0
        curr_idx = 0
        curr_string = ""
        while curr_idx < len(s):
            if s[curr_idx] == "@":
                # print("curr_idx caught @", curr_idx)
                count = int(count_str)
                count_str = ""
                # print("count bound by @: ", count)
            else:
                count_str += s[curr_idx]
                curr_idx += 1
                start_idx = curr_idx
                continue
            while count is not None and curr_idx < len(s) and curr_idx - start_idx <= count:
                curr_string += s[curr_idx]
                curr_idx += 1
            
            str_list.append(curr_string[1:] if len(curr_string) > 1 else "")
            count = None
            if curr_idx >= len(s):
                break
            # print("curr_idx: ", curr_idx)
            # print("start_idx: ", start_idx)
            # print("str_list: ", str_list)
            start_idx = curr_idx
            curr_string = ""
            # print("new_start: ", start_idx)
            # print("rest of string: ", s[curr_idx:])
        return str_list



