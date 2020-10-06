# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        to_visit = [node]
        visited = {}
        graph = {}
        
        while to_visit:
            this_node = to_visit.pop(0)
            if this_node not in visited:
                my_node = Node(this_node.val, this_node.neighbors)
                visited[this_node] = my_node
                graph[this_node.val] = [n.val for n in my_node.neighbors]
                to_visit.extend(this_node.neighbors)
        
        mapped_with_node = {}
        
        for key,val in graph.items():
            mapped_with_node[key] = Node(key)
        
        for key,_ in mapped_with_node.items():
            for j in graph[key]:
                mapped_with_node[key].neighbors.append(mapped_with_node[j])
        
        return mapped_with_node[1]
