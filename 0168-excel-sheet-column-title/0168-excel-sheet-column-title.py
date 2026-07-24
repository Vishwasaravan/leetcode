class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnTitle=''
        while columnNumber>0:
            columnNumber-=1
            columnTitle=chr(columnNumber%26+ord('A'))+columnTitle
            columnNumber//=26
        return columnTitle