class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = []
        d = {}

        for s in strs:
            myKey = ''.join(sorted(s))
            if myKey in d:
                d[myKey].append(s)
            else:
                d[myKey] = [s]

        for value in d.values():
            x.append(value)

        return x
        