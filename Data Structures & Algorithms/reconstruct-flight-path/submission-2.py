class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        vertMap = { src: [] for src, dst in tickets}

        tickets.sort()

        for dep,arr in tickets:
            if dep not in vertMap:
                vertMap[dep] = []
            
            vertMap[dep].append(arr)

        res = ["JFK"]
        
        def dfs(root):
            if len(res) == len(tickets) +1:
                return True
            if root not in vertMap:
                return False
            
            for i,dest in enumerate(vertMap[root]):
                print(dest)

                vertMap[root].pop(i)
                res.append(dest)
                if dfs(dest): return True
                vertMap[root].insert(i,dest)
                res.pop()

            
            return False


            


            

            
        dfs("JFK")
        return res