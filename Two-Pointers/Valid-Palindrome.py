class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Initialize a pointer for each side to increment from
        leftPointer = 0
        rightPointer = len(s) - 1

        # Stop when the pointers meet
        while leftPointer < rightPointer:

            # Skip non-alphanumeric characters and stop when the pointers meet
            while not self.isAlphaNumeric(s[leftPointer]) and leftPointer < rightPointer:
                leftPointer += 1

            while not self.isAlphaNumeric(s[rightPointer]) and leftPointer < rightPointer:
                rightPointer -= 1

            # Compare the values and return false if they differ
            if s[leftPointer].lower() != s[rightPointer].lower():
                return False 

            leftPointer += 1
            rightPointer -= 1

        # If we make it through the whole string without differences, it is a valid palindrome
        return True

    def isAlphaNumeric(self, character):
        
        return (ord('A') <= ord(character) <= ord('Z') or 
                ord('a') <= ord(character) <= ord('z') or 
                ord('0') <= ord(character) <= ord('9'))