class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        graph = {}
        graph1 = {}
        if trust == [] and N == 1:
            return N
        
        for i in trust:
            if i[1] not in list(graph.keys()):
                graph[i[1]] = [i[0]]
            else:
                graph[i[1]].append(i[0])

            if i[0] not in list(graph1.keys()):
                graph1[i[0]] = [i[1]]
            else:
                graph1[i[0]].append(i[1])
                
        for i in list(graph.keys()):
            key = i
            if len(graph[key]) == N-1 and key not in graph[key] and (key not in graph1 or graph1[key] == []):
                return key
        return -1
