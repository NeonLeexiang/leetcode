class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = int('-'+str(abs(x))[::-1]) if x < 0 else int(str(abs(x))[::-1])
        return r if abs(r) < 2**31 else 0
