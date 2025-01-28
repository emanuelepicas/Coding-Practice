class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        pre_value = 0

        for char in reversed(s):
            value = roman[char]
            if value < pre_value:
                total -= value
            else:
                total += value
            pre_value = value    

        return total




def test_examples():
    solution = Solution()

    # Test cases with varying lenghts

    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994), 
    ]

    for roman, expected in test_cases:
        result = solution.romanToInt(roman)
        print(f"romanToInt({roman}) == {result} [expected: {expected}]")


if __name__ == "__main__":
    test_examples()