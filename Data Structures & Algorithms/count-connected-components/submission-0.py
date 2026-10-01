class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        output = []

        vMap = {i:[] for i in range(n)}

        for v1,v2 in edges:
            vMap[v1].append(v2)
            vMap[v2].append(v1)
        
        visited = set()


        def dfs(root,prev, comp):
            if root in comp:
                return
            if root in visited:
                return
            
            comp.add(root)
            visited.add(root)

            for pr in vMap[root]:
                if pr == prev:
                    continue
                dfs(pr,root,comp)

        for key in vMap:
            resulting_set = set ()
            dfs(key,-1,resulting_set)
            if len(resulting_set) !=0:
                output.append(resulting_set)

        return len(output)  