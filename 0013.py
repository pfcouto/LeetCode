class Solution:
    def romanToInt(self, s: str) -> int:

        # Symbol       Value
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        # I can be placed before V(5) and X (10) to make 4 and 9.
        # X can be placed before L(50) and C (100) to make 40 and 90.
        # C can be placed before D(500) and M(1000) to make 400 and 900.

        romanToDecimalMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        value = 0
        n = len(s)

        for i in range(n):

            if i == n-1 or romanToDecimalMap[s[i]] >= romanToDecimalMap[s[i+1]]:
                value += romanToDecimalMap[s[i]]
            else:
                value -= romanToDecimalMap[s[i]]

        return value


print(Solution().romanToInt("XX"))
