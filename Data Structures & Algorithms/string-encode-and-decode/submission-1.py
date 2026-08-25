class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += f'{len(s)}#{s}'
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            length = 0
            while i < len(s) and s[i].isdigit():
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            cur = ""
            for _ in range(length):
                cur += s[i]
                i += 1
            ret.append(cur)

        return ret