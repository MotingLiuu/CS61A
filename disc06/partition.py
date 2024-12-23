def partition(n, m):
    if n == 0:
        return True
    if n < 0 or m <= 0:
        return False
    if n > 0:
        left = partition(n - m, m)
        right = partition(n, m - 1)
        return [m, left, right]

def printPartition(partitionTree, partition = []):
    if partitionTree == True:
        print(partition)
    elif partitionTree == False:
        return
    else:
        left = partitionTree[1]
        right = partitionTree[2]
        printPartition(left, partition + [partitionTree[0]])
        printPartition(right, partition)

printPartition(partition(6, 4))