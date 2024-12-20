def partition(n: int, m: int):
    partitionTree = []
    def consTree(n: int, m: int, pos: list):
        if n == m:
            pos = 'True'
        if n > m:
            pos.append([])
        else:
            pos = 'False'
        if m > 1:
            consTree(n, m - 1, pos[1])
            