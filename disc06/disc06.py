def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

print((lambda t: [next(t) for _ in range(10)])(gen_fib())) 

print(next(filter(lambda n: n > 2024, gen_fib())))

def partition_gen(n, m):
    assert n > 0 and m > 0
    if n == m:
        yield [m]
    if n - m > 0:
        for partition in partition_gen(n - m, m):
            yield [m] + partition
    if m > 1:
        for partition in partition_gen(n, m - 1):
            yield partition
        
for partition in (partition_gen(6, 4)):
    print(partition)
    
    