def solveHanoi(n, start, end, temp):
    if n > 0:
        solveHanoi(n-1, start, temp, end)
        end.insert(0, start.pop(0))
        solveHanoi(n-1, temp, end, start)
