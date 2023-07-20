def f(*args):
    results = []
    for i in args:
        results.append(i * i)
    return results


numbers = [1, 2, 3, 4]
print(f(*list(range(100))))
