class Solution:
    def toLowerCase(self, s: str) -> str:
        return(''.join([i.lower() if i.isupper() else i for i in s]))
        