class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        output = []

        visited = set()

        cycle = set()

        
        preMap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        
        def dfs(root):
            if root in cycle:
                return False
            if root in visited:
                return True
            
            cycle.add(root)

            for pre in preMap[root]:
                if dfs(pre) == False:
                    return False
            
            visited.add(root)
            cycle.remove(root)
            output.append(root)
        
        for key in preMap:
            if dfs(key) == False:
                return []
        
        return output
        