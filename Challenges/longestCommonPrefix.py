class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        

        # Get the shortest string length to avoid index out of bounds
        shortest = min(len (s) for s in strs)

        for i in range(shortest):

            char = strs[0][i]


            for string in strs[1]:
                if string[i] != char:

                    return strs[0][:i]

        return strs[0][:shortest]