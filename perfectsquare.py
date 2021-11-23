class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        for i in range(1,A+1):
            if i*i == A:
                return i
            else:
                if i*i >A:
                    return -1
s=Solution()
print(s.solve(16))
