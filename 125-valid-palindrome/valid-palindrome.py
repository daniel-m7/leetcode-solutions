class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^A-Za-z0-9]', '', s).upper()
        r, l = 0, len(s) - 1
        while r < l:
            if s[r] != s[l]:
                return False
            r += 1 
            l -= 1
        return True