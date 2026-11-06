class Solution:
    def _dfs(self, graph, visited, node):
        if visited[node] == True:
            return
        visited[node] = True
        for n in graph[node]:
            self._dfs(graph, visited, n)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        visited = []
        graph = {}
        
        ## O(n)
        for i in range(n):
            visited.append(False)
            graph[i] = []
        
        ## O(e)
        for e in edges:
            n1,n2 = e[0],e[1]
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        ## O(n+e)
        self._dfs(graph, visited, 0)

        ## O(n)
        return False not in visited