class Solution(object):
    def solve(self, groups):
        size = len(groups)
        if size == 1: return groups[0]
        ngroups = []
        for x in range(size / 2):
            ngroups.append('(' + groups[x] + ',' + groups[size - x - 1] + ')')
        return self.solve(ngroups)

    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.solve(map(str, range(1, n + 1)))
val=Solution()
n=int(input())
print(val.findContestMatch(n))
