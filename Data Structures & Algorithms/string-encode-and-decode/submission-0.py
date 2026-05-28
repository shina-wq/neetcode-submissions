from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.

        Format:
            <length>#<string>

        Example:
            ["hi", "abc"] -> "2#hi3#abc"
        """

        encoded = []

        for s in strs:
            encoded.append(f"{len(s)}#{s}")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """
        Decodes the encoded string back into the original list.
        """

        result = []
        i = 0

        while i < len(s):

            # Find the separator '#'
            j = i

            while s[j] != '#':
                j += 1

            # Extract string length
            length = int(s[i:j])

            # Move pointer to start of actual string
            j += 1

            # Extract the string using the known length
            word = s[j:j + length]

            result.append(word)

            # Move pointer to next encoded string
            i = j + length

        return result