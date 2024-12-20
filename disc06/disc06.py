def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

print((lambda t: [next(t) for _ in range(10)])(gen_fib())) 

print(next(filter(lambda n: n > 2024, gen_fib())))