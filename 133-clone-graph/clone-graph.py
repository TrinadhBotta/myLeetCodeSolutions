from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        queue = deque([])
        queue.append(node)
        clone = Node(node.val)
        d = {}
        d[1] = clone
        seen = set()
        while queue:
            main_node = queue.popleft()
            clone_node = d[main_node.val]
            if len(main_node.neighbors)>0:
                for neighbor_node in main_node.neighbors:
                    if (main_node.val,neighbor_node.val) not in seen:
                        if neighbor_node.val not in d:
                            new_node = Node(neighbor_node.val)
                            d[neighbor_node.val] = new_node
                        else:
                            new_node = d[neighbor_node.val]
                        clone_node.neighbors.append(new_node)
                        new_node.neighbors.append(clone_node)
                        queue.append(neighbor_node)
                        seen.add((main_node.val,neighbor_node.val))
                        seen.add((neighbor_node.val,main_node.val))
        return(clone)