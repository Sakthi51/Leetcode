class Solution:
    def reverseWords(self, s: str) -> str:
        to_store = ''
        string = s.split()
        print(string)
        for i in string:
            to_store += i[::-1] + ' '
        return to_store[:-1]

        