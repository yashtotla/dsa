from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indeg = defaultdict(int)
        chars = set()

        for w in words:
            chars.update(w)
        
        for a, b in zip(words, words[1:]):
            if a[:len(b)] == b and len(a) > len(b):
                return ""
            for x, y in zip(a, b):
                if x != y:
                    if y not in graph[x]:
                        graph[x].add(y)
                        indeg[y] += 1
                    break
        
        q = deque(c for c in chars if indeg[c] == 0)
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for n in graph[c]:
                indeg[n] -= 1
                if indeg[n] == 0:
                    q.append(n)
        
        return "".join(order) if len(order) == len(chars) else ""