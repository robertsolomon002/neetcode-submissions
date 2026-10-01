class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n +1)]

        rank = [1] *(n+1)


        def find(node):
            rNode = node

            while parent[rNode] != rNode:
                parent[rNode] = parent[parent[rNode]]
                rNode = parent[rNode]

            return rNode
        
        def union(n1,n2):

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
        
        for v1,v2 in edges:
            if union(v1,v2) ==0:
                return [v1,v2]
        