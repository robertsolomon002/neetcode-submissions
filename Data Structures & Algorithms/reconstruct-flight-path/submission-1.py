class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        verMap = {}
        
        tickets.sort()

        for dep,arr in tickets:
            if dep not in verMap:
                verMap[dep] = []
            verMap[dep].append(arr)
        
        print(verMap)
        visited = set()
        res =["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in verMap:
                return False
            temp = list(verMap[src])
            for i,v in enumerate(temp):
                verMap[src].pop(i)
                res.append(v)

                if dfs(v) :return True
                res.pop()
                verMap[src].insert(i,v)
            return False
        dfs("JFK")
        return res

        


        
        return res
        