# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        final_s = ''.join([char for char in lower_s if char.isalnum()])

        reversed_s = final_s[::-1]

        if reversed_s == final_s:
            return True
        return False