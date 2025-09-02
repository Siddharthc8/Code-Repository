import random as r

r.random()                # 0 to 1 random float values      1 exclusive
r.uniform(0,10)     # 0 to 10 random float values      10 exclusive
r.randint(0,10)     # 0 to 10 random integer values    both inclusive
r.choice([1,2,3,4,5,6,7,8,9])

# Example
# name = "Sid"
# greetings = ['Hello', "Hi", "Hola", "Howdy", "Hey"]
# greeting = r.choice(greetings)
# print(greeting, name)

colors = ['red', 'green', 'blue', "yellow"]
color = r.choices(colors,weights=[10, 10, 2, 8], k=10)
print(color)

deck = list(range(1,53))
r.shuffle(deck)
hand = r.sample(deck, k=5)
print(deck)
print(hand)