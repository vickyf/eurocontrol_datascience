import collections as c
name = "John Doe"
name_count = c.Counter(name)
print(name_count)

zoo = ["monkey","elephant","monkey","monkey","elephant","lion","monkey","zebra","polar bear","elephant","monkey","zebra"]
animals = c.Counter(zoo)
print(animals)
print(animals.most_common(1))