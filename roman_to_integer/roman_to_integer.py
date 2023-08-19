class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        RomanNum = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        for i in range(len(s)):
            if i < len(s) - 1 and RomanNum[s[i]] < RomanNum[s[i+1]]:
                total -= RomanNum[s[i]]
            else:
                total += RomanNum[s[i]]

        return total