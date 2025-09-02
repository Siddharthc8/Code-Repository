from collections import defaultdict, Counter

def maxNumberOfBalloons(text: str):
    count = defaultdict(int)   # Does not throw error when not in dict already instead assumes it already assigned to 0

    for c in text:
        count[c] += 1

    return min(count["b"], count["a"], count["l"]//2, count["o"]//2, count["n"],)


#
def counter(text: str):
    count = Counter(text)

    return min(count["b"], count["a"], count["l"]//2, count["o"]//2, count["n"],)