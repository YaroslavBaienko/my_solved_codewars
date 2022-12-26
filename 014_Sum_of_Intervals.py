def sum_of_intervals(intervals):
    from collections import Counter
    interval = []
    length = 0
    for i in range(len(intervals)):
        for j in range(len(intervals[i])):
            for x in range(intervals[i][j], intervals[i][j+1]):
                interval.append(x)
            break

    numbers = Counter(interval)

    for k in numbers:
        length += 1

    return length

print(sum_of_intervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ))