from collections import defaultdict
from collections import Counter

text = "Musk was born and grew up in Pretoria, South Africa. He attended the University of Pretoria before moving to Canada at age 17, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University and transferred to the University of Pennsylvania, where he received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University but decided to instead pursue a business career, co-founding the web software company Zip2 with his brother, Kimbal. The startup was acquired by Compaq for $307 million in 1999. The same year, Musk co-founded the online bank X.com, which merged with Confinity in 2000 to form PayPal. eBay bought PayPal in 2002 for $1.5 billion."

def good_way():
    word_count_dict = {}

    for word in text.split(" "):
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    print(word_count_dict)

def better_way():
    word_count_dict = defaultdict(int)
    for word in text.split(" "):
        word_count_dict[word] += 1

    print(word_count_dict)

def best_way():
    word_count_dict = Counter()
    for word in text.split(" "):
        word_count_dict[word] += 1

    print(word_count_dict)


if __name__ == '__main__':
    good_way()
    better_way()
    best_way()