"""Merge Overlapping Subintervals"""

def merge(intervals):
    n = len(intervals)
    intervals.sort()
    ans = []

    for i in range(n):
        if len(ans) == 0 or intervals[i][1] > ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    return ans


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))