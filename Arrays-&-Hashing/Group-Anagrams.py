class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # Create dict to store final charCountSignature:string list pairs
        anagramDict = {}

        for str in strs:

            # Count each character
            charList = [0] * 26
            for char in str:
                charList[ord(char) - ord("a")] += 1
            charList = tuple(charList)

            # Either create a new charCountSignature:string list pair, or add to existing
            if charList in anagramDict:
                anagramDict[charList].append(str)
            else:
                anagramDict.update({charList:[str]})
                
        return anagramDict.values()  