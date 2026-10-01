class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = set()

        vMap = {i:[] for i in range(n)}

        for v1,v2 in edges:
            vMap[v1].append(v2)
            vMap[v2].append(v1)
        
        def dfs(root,prev):
            if root in visited:
                return False
            
            visited.add(root)

            for v2 in vMap[root]:
                if v2 == prev:
                    continue
                if not dfs(v2, root):
                    return False
            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n
