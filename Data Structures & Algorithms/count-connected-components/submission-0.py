class Solution:
    def _dfs(self, graph, visited, node):
        if visited[node] is True:
            return
        visited[node] = True
        for child in graph[node]:
            self._dfs(graph, visited, child)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = []
        graph = {}

        for i in range(n):
            visited.append(False)
            graph[i] = []
        
        for e in edges:
            e1,e2 = e[0],e[1]
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        count = 0
        for i in range(n):
            if visited[i] is True:
                continue
            count += 1
            self._dfs(graph, visited, i)
        
        return count