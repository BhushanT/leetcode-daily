"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
October 24th, 2024 Leetcode 1233
Leetcode Medium
Time Taken to Complete: N/A Needed Hint
Runtime: 26 ms | Beats 93.10%
Memory: 29.53 MB | Beats 93.10%
Time Complexity: NlogN

"""

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        
        folders.sort()
        result = [folders[0]]
        for folder in folders:
            if folder == folders[0]:
                continue
            prev_folder = result[-1]
            prev_folder += "/"

            if not folder.startswith(prev_folder):
                result.append(folder)

        return result