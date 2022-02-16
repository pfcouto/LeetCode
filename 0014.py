class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        prefix = ""

        for i in range(len(min(strs))):
            temp = strs[0][i]
            if all(a[i] == temp for a in strs):
                prefix += temp
            else:
                break

        return prefix
