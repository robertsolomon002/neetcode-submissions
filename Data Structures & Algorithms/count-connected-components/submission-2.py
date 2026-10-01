class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        output = 0

        vMap = {i:[] for i in range(n)}

        for v1,v2 in edges:
            vMap[v1].append(v2)
            vMap[v2].append(v1)
        
        visited = set()


        def dfs(root,prev):
            if root in visited:
                return
            

            visited.add(root)

            for pr in vMap[root]:
                if pr == prev:
                    continue
                dfs(pr,root)

        for key in vMap:
            if key not in visited:
                
                dfs(key,-1)
                output += 1
                

        return output