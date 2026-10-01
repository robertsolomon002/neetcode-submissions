class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True


        vertMap = { i: [] for i in range(n)}

        for v1,v2 in edges:
            vertMap[v1].append(v2)
            vertMap[v2].append(v1)
        
        cycle = set()
        #visited = set()
        

        def dfs(root,prev):

            if root in cycle:
                return False
            
            #if vertMap[root] == []:
                #return True
            
            cycle.add(root)

            for pre in vertMap[root]:
                if pre == prev:
                    continue
                if not dfs(pre,root):
                    return False
            
            #cycle.remove(root)
            #visited.add(root)
            #vertMap[root] = []
            return True 



        
        if not dfs(0,-1):
            return False
        print(cycle)
        return len(cycle) == n

