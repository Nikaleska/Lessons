from itertools import chain
#
#
# def get_children(users):
#     childrens = map(lambda user: user['children'], users)
#     return list(chain.from_iterable(childrens))
#
# users = [
#     {
#         'name': 'Tirion',
#         'children': [
#             {'name': 'Mira', 'birthday': '1983-03-23'},
#         ],
#     },
#     {'name': 'Bronn', 'children': []},
#     {
#         'name': 'Sam',
#         'children': [
#             {'name': 'Aria', 'birthday': '2012-11-03'},
#             {'name': 'Keit', 'birthday': '1933-05-14'},
#         ],
#     },
#     {
#         'name': 'Rob',
#         'children': [
#             {'name': 'Tisha', 'birthday': '2012-11-03'},
#         ],
#     },
# ]
#
# print(get_children(users))

# def get_girl_friends(users):
#     friends = chain.from_iterable(map(lambda user: user['friends'], users))
#     girl_friends = filter(lambda friend: friend['gender'] == 'female', friends)
#     return list(girl_friends)
#
# users = [
#     {
#         'name': 'Tirion',
#         'friends': [
#             {'name': 'Mira', 'gender': 'female'},
#             {'name': 'Ramsey', 'gender': 'male'},
#         ],
#     },
#     {'name': 'Bronn', 'friends': []},
#     {
#         'name': 'Sam',
#         'friends': [
#             {'name': 'Aria', 'gender': 'female'},
#             {'name': 'Keit', 'gender': 'female'},
#         ],
#     },
#     {
#         'name': 'Rob',
#         'friends': [
#             {'name': 'Taywin', 'gender': 'male'},
#         ],
#     },
# ]
#
# print(get_girl_friends(users))

from functools import reduce


def group_by(items, key):
    def group_by_key(acc, item):
        if item[key] not in acc:
            acc[item[key]] = []
        acc[item[key]].append(item)
        return acc
    return reduce(group_by_key, items, {})


students = [
    {'name': 'Tirion', 'class': 'B', 'mark': 3},
    {'name': 'Keit', 'class': 'A', 'mark': 3},
    {'name': 'Ramsey', 'class': 'A', 'mark': 4},
]

print(group_by(students, 'mark'))


def validate_passwords(password_list):
    result = (
        all(len(password)>8 for password in password_list)
        and any(any(char.isdigit() for char in password) for password in password_list)
        and any(any(char.isupper() for char in password) for password in password_list)
        and all(' ' not in password for password in password_list)
    )
    return result