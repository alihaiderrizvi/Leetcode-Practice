class Solution:
    def decodeString(self, s: str) -> str:
        # open_bkt = 0
        num_start = 0
        num_end = 0
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                num_start = i
                while s[i].isnumeric():
                    i += 1
                num_end = i
                # open_bkt = i

            if s[i] == ']':
                # sample = s[open_bkt+1:i] * int(s[num_start:num_end])
                s = s.replace(s[num_start:i+1], s[num_end+1:i] * int(s[num_start:num_end]))
                i = -1
            i += 1
        return s
