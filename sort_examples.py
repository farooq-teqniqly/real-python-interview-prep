animals = [
    dict(type="cat", name="Sifu", age=4),
    dict(type="dog", name="Bertie", age=10),
    dict(type="hamster", name="Rollo", age=1),
]

print(sorted(animals, key=lambda a: a["age"]))
print(sorted(animals, key=lambda a: a["age"], reverse=True))

# Original list is not mutated by sorted()
print(animals)

# Mutate the original list
animals.sort(key=lambda a: a["age"])
print(animals)