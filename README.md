# Useful Python Tips and Tricks Every Programmer Should Know
## **Minimize for loop usage**

There are three popular ways to write a for loop in Python

❌ bad way

    x = [0, 2, 4, 6, 8, 10]
    sum_squared = 0

    for i in range(len(x)):
        sum_squared += x[i] ** 2
    print(sum_squared)

✅ good way

    def good_way():
    x = [0, 2, 4, 6, 8, 10]
    sum_squared = 0

    for y in x:
        sum_squared += y ** 2
    print(sum_squared)  

🐍 python way

    x = [0, 2, 4, 6, 8, 10]
    sum_squared = sum([y**2 for y in x])
    print(sum_squared)

