class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ""
        for item in strs:
            encoded += str(len(item)) + "#" + item

        return encoded

    def decode(self, encoded: str) -> List[str]:
        if not encoded:
            return []

        decoded = []
        left = 0
        while left < len(encoded):
            right = left
            while encoded[right] != '#':
                right += 1
            item_lenght = int(encoded[left:right])
            start = right + 1
            end = start + item_lenght            
            decoded.append(encoded[start : end])
            left = end

        return decoded

