# Useful Python Tips and Tricks Every Programmer Should Know
** Minimize for loop usage **

There are three popular ways to write a for loop in Python

❌ bad way

    x = [0, 2, 4, 6, 8, 10]
    sum_squared = 0

    for i in range(len(x)):
        sum_squared += x[i] ** 2
        
    print(sum_squared)

✅ good way

🐍 python way

