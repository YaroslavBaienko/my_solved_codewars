def sum_of_intervals(intervals):
    result = set()

    for (start, end) in intervals:
        result.update(set(range(start, end)))

    return len(result)

print(sum_of_intervals( [
   [0, 20],
   [-100000000, 10],
   [30, 40]
] ))