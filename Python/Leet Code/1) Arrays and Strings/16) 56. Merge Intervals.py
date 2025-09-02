# With O(n log n) and O(n)
def merge(intervals):
    start = 0
    end = 1
    res = []
    intervals = sorted(intervals)
    for i in range(len(intervals)):
        if not res or res[-1][end] <  intervals[i][start]:
            res.append(intervals[i])
        else:
            res[-1][end] = max(res[-1][end], intervals[i][end])
    print (res)



# with O(n log n) and O(1)
def merge1(intervals):
    start = 0
    end = 1
    k = 0
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[k][end] >= intervals[i][start]:
            intervals[k][end] = max(intervals[k][end], intervals[i][end])
        else:
            k += 1
            intervals[k] = intervals[i]
    print(intervals[:k+1])


intervals = [[1,3],[2,6],[8,10],[15,18]]
inter = [[1,4],[0,4]]

merge1(intervals)
merge1(inter)
