class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        maxlen = left = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left = left + 1
            chars.add(s[right])
            maxlen = max(maxlen, right - left + 1)
        return maxlen
