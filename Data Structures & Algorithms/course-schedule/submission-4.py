class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        

        for course,preq in prerequisites:
            preMap[course].append(preq)


        visited = set()

        def dfs(root):
            if root in visited:
                return False
            if preMap[root] == []:
                return True
            
            visited.add(root)

            for crs in preMap[root]:
                if not dfs(crs) : return False


            visited.remove(root)
            preMap[root] = []
            return True
        
        for key in preMap:
            if dfs(key) == False:
                return False
        
        return True