class Solution:
    def removeStars(self, s: str) -> str:
        # have to remove closest star and remove the left element
        result = ''
        for i in s:
            if i.isalpha():
                result += i
            elif i == "*":
                result = result[:-1]
        return result

                

        