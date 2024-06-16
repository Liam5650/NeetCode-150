class Solution:

    def encode(self, strs: list[str]) -> str:
        
        joined = ""
        for string in strs:
            # We need to create a delimiter. Using just a number at the start of the word
            # won't work if the string size is more than 1 digit, so we use a symbol as a second
            # delimiter to tell the decoder when to stop reading the string length int delimiter.
            # We also put this delimiter at the start of the string to make sure it is the first thing
            # read by the decoder, and not the start of a string which would contain similar characters.
            joined += str(len(string)) + "^" + string

        return joined

    def decode(self, s: str) -> list[str]:
        
        separated = []
        i = 0

        while i < len(s):

            # Decode the length of the sub string
            length = ""
            while s[i] != '^':
                length += s[i]
                i += 1
            length = int(length)

            # Append the sliced string and advance the pointer to the start of the next delimiter
            separated.append(s[i+1:i+length+1])
            i += length + 1
        
        return separated