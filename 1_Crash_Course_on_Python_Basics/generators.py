def fibonacci(max=1):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


a = fibonacci(1000)
lst = []
while True:
    try:
        lst.append(next(a))
    except StopIteration:
        break
print(lst)