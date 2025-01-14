from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = [0] * len(A)
        seen = set()  # Tracks elements seen in A and B prefixes
        common_count = 0  # Tracks number of common elements
        
        for i in range(len(A)):
            if A[i] in seen:
                common_count += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                common_count += 1
            else:
                seen.add(B[i])
            
            ans[i] = common_count
        
        return ans
