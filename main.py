# print("Hello World")
#
# def id_generator(prefix: str) -> str:
#     counter = 0
#
#     def id_generator():
#         nonlocal counter
#         counter += 1
#         return f'{prefix}-{counter:03d}'
#
#     return id_generator
#
#
# def get_stock(inventory, item):
#     return inventory.get(item, 0)
#
#
# def update_inventory(inventory, item, quantity):
#     if item in inventory:
#         inventory[item] += quantity
#     else:
#         inventory[item] = quantity
#
#     return inventory
#
# inventory = {}
# update_inventory(inventory, "apple", 10)
# print(get_stock(inventory, "apple"))
# update_inventory(inventory, "banana", 5)
# print(get_stock(inventory, "banana"))
# update_inventory(inventory, "banana", 2)
# print(get_stock(inventory, "banana"))
#
# print(inventory)
#
#
# def get_average(*numbers):
#     if not numbers:
#         return None
#     result = sum(numbers) / len(numbers)
#
#     return result


def format_person_info(name, age, **kwargs):
    user_info = f"Name: {name}, Age: {age}"
    for key, value in sorted(kwargs.items()):
        user_info += f", {key.capitalize()}: {value}"
    return user_info

# def format_person_info(name, age, **kwargs):
#     base_info = f"Name: {name}, Age: {age}"
#     additional_info = []
#     for key, value in sorted(kwargs.items()):
#         additional_info.append(f"{key.capitalize()}: {value}")
#         return f"{base_info}, {", ".join(additional_info)}"
#     else:
#         return base_info

def take_last(string, number):
    if not string or len(string) < number:
        return None

    result = lambda number: string[-number:]
    return result(number)[::-1]

print(take_last("hexlet", 3))


def get_first_name(user_info):
    return user_info.split("_")[0]


def sort_by(key_function, users):
    return sorted(users, key=key_function)

users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

sort_by(get_first_name, users)  # ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]
print(users) # => ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

def memoized(func):
    cache = {}

    def wrapper(number):
        if number not in cache:
            cache[number] = func(number)

        return cache[number]

    return wrapper

@memoized
def f(x):
    print('Calculating...')
    return x * 10

print(f(1))


def get_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = get_fibonacci()

for x in fib:
    print(x)
    if x > 10:
        break

from itertools import chain

def get_children(users):
    children = []
    for user in users:
        children.append(user["children"])
    return list(chain.from_iterable(children))

users = [
    {
        'name': 'Tirion',
        'children': [
            {'name': 'Mira', 'birthday': '1983-03-23'},
        ],
    },
    {'name': 'Bronn', 'children': []},
    {
        'name': 'Sam',
        'children': [
            {'name': 'Aria', 'birthday': '2012-11-03'},
            {'name': 'Keit', 'birthday': '1933-05-14'},
        ],
    },
    {
        'name': 'Rob',
        'children': [
            {'name': 'Tisha', 'birthday': '2012-11-03'},
        ],
    },
]

print(get_children(users))