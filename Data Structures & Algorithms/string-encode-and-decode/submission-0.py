class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            for c in s:
                output+= str(ord(c))
                output+= ','
            output+= '.'
        return output

    def decode(self, s: str) -> List[str]:
        list = []
        words = s.split('.')[:-1]
        for word in words:
            list_item = ""
            ascii_chars = word.split(',')[:-1]
            for c in ascii_chars:
                list_item += chr(int(c))
            list.append(list_item)
        return list
