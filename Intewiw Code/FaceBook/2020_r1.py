from bisect import insort

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        maxmin = {"max":0, "min":0}
        self.allChilds(root, 0, maxmin)
        res = [[] for _ in range(-maxmin["min"] + maxmin["max"] + 1)]
        self.BFS(root, res, -maxmin["min"])
        for i in range(len(res)):
            concatenated = []
            for arr in res[i]: concatenated.extend(arr)
            res[i] = concatenated
        return res
    
    def BFS(self, root, res: List[List[int]], level: int):
        list_ = [[root, level, 0]]
        while list_:
            node, lvl, deep = list_[0][0], list_[0][1], list_[0][2]
            list_.pop(0)
            if node:
                try: res[lvl][deep]
                except: 
                    for _ in range(deep - len(res[lvl]) + 1): res[lvl].append([])            
                insort(res[lvl][deep], node.val)
                list_.append([node.left, lvl - 1, deep + 1])
                list_.append([node.right, lvl + 1, deep + 1])
            
        
    def allChilds(self, root, level, maxmin):
        if root is None: return
        maxmin["max"] = max(maxmin["max"], level)
        maxmin["min"] = min(maxmin["min"], level)
        self.allChilds(root.left, level - 1, maxmin)
        self.allChilds(root.right, level + 1, maxmin)