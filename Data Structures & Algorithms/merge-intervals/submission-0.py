class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            if not merged:
                merged.append([start, end])
            ps, pe = merged[-1][0], merged[-1][1]
            if start > pe:
                merged.append([start, end])
            else:
                merged[-1][1] = max(end, pe)
        return merged