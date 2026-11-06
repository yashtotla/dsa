from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pcount = {}
        waiting = {}
        for i in range(numCourses):
            pcount[i] = 0
            waiting[i] = []

        for p in prerequisites:
            c1, c2 = p[0], p[1]
            pcount[c1] += 1
            waiting[c2].append(c1)
        
        courses_taken = 0
        q = deque()
        for k,v in pcount.items():
            if v == 0:
                q.append(k)
        
        while len(q) > 0:
            course = q.popleft()
            courses_taken += 1
            for c in waiting[course]:
                pcount[c] -= 1
                if pcount[c] == 0:
                    q.append(c)
        
        return courses_taken == numCourses