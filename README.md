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

## **How to count the number of word occurrences in a paragraph**

✅ good way

    text = "Musk was born and grew up in Pretoria, South Africa. He attended the University of Pretoria before moving to Canada at age 17, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University and transferred to the University of Pennsylvania, where he received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University but decided to instead pursue a business career, co-founding the web software company Zip2 with his brother, Kimbal. The startup was acquired by Compaq for $307 million in 1999. The same year, Musk co-founded the online bank X.com, which merged with Confinity in 2000 to form PayPal. eBay bought PayPal in 2002 for $1.5 billion."
    word_count_dict = {}

    for word in text.split(" "):
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    print(word_count_dict)  


