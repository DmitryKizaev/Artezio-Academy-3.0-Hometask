"""Homework 6 Part 2 Generators Task 3"""

# Есть два списка разной длины, в одном ключи,
# в другом значения. Составить словарь.
# Для ключей, для которых нет значений использовать None
# в качестве значения. Значения, для которых нет ключей игнорировать.


def dict_generate(l_keys, l_values):
    """Составляет словарь из 2 списков, основываясь на ключах"""
    while len(l_keys) > len(l_values):
        l_values.append(None)
    return {key: value for key, value in zip(l_keys, l_values)}

print("Values:")
ATTR = ["zero", "one", "two", "three", "four"]
print(ATTR)
print("Keys:")
IDS = [i for i in range(len(ATTR))]
print(IDS)

print("Dictionary generated:")
print(dict_generate(IDS, ATTR), "\n")

print("New keys:")
IDS = [i for i in range(8)]
print(IDS)
print("Dictionary generated:")
print(dict_generate(IDS, ATTR), "\n")

print("New values:")
ATTR = ["zero", "one", "two", "three", "four", "five", "one", "two", "three", "four", "five"]
print(ATTR)
print("Dictionary generated:")
print(dict_generate(IDS, ATTR))
