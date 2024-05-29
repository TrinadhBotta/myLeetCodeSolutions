"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return(None)

        head = Node(node.val)
        t = head
        d = {}
        d[node.val] = t

        seen = set()
        stack = [node]

        while len(stack)>0:
            cur_node = stack.pop()

            for neighbor in cur_node.neighbors:

                if (cur_node.val,neighbor.val) in seen or (neighbor.val, cur_node.val) in seen:
                    continue
                
                if neighbor.val not in d:
                    new_neighbor = Node(neighbor.val)
                    d[neighbor.val] = new_neighbor

                d[cur_node.val].neighbors.append(d[neighbor.val])
                d[neighbor.val].neighbors.append(d[cur_node.val])
                stack.append(neighbor)
    
                seen.add((cur_node.val,neighbor.val))
        
        return(head)




        