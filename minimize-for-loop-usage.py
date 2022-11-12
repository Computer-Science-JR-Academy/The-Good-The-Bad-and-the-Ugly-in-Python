def bad_way():
    x = [0, 2, 4, 6, 8, 10]
    sum_squared = 0

    for i in range(len(x)):
        sum_squared += x[i] ** 2
    print(sum_squared)

def good_way():
    x = [0, 2, 4, 6, 8, 10]
    sum_squared = 0

    for y in x:
        sum_squared += y ** 2
    print(sum_squared)

def python_way():
    x = [0, 2, 4, 6, 8, 10]
    sum_squared = sum([y**2 for y in x])
    print(sum_squared)

if __name__ == '__main__':
    bad_way()
    good_way()
    python_way()