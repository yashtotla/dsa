class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * (n+1)
        dist[k] = 0

        for _ in range(0, n-1):
            changed = False
            for u,v,w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:
                break

        ans = max(dist[1:])
        return -1 if ans == INF else ans
