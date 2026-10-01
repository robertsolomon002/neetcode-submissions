class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]* n

        def find(node):
            return_node = node

            while parent[return_node] != return_node:
                parent[return_node] = parent[parent[return_node]]
                return_node = parent[return_node]

            return return_node
        
        def unione(n1,n2):
            p1,p2 = find(n1),find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            return 1
        
        res = n

        for v1,v2 in edges:
            res -= unione(v1,v2)

        return res