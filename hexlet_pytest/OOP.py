# def change_owner(node, owner):
#     name = fs.get_name(node)
#     new_meta = copy.deepcopy(fs.get_meta(node))
#     new_meta["owner"] = owner
#     if fs.is_file(node):
#         # Возвращаем обновленный файл
#         return fs.mkfile(name, new_meta)
#     children = fs.get_children(node)
#     # Ключевая строчка
#     # Вызываем рекурсивное обновление каждого потомка
#     new_children = list(map(lambda child: change_owner(child, owner), children))
#     new_tree = fs.mkdir(name, new_children, new_meta)
#     # Возвращаем обновленную директорию
#     return new_tree
#
# def downcase_file_names(node):
#     new_meta = copy.deepcopy(get_meta(node))
#     name = get_name(node)
#     if is_file(node):
#         return mkfile(name.lower(), new_meta)
#     children = get_children(node)
#     new_children = map(downcase_file_names, children)
#     return mkdir(name, list(new_children), new_meta)
#
# def get_nodes_count(node):
#     if fs.is_file(node):
#         # Возвращаем 1 для учета текущего файла
#         return 1
#     # Если узел — директория, получаем его потомков
#     children = fs.get_children(node)
#     # Самая сложная часть
#     # Считаем количество потомков для каждого потомка,
#     # вызывая рекурсивно нашу функцию get_nodes_count
#     descendant_counts = list(map(get_nodes_count, children))
#     # Возвращаем 1 (текущая директория) + общее количество потомков
#     return 1 + sum(descendant_counts)
#
#
# # # Моё решение
# # def get_hidden_files_count(node):
# #     if is_file(node):
# #       if get_name(node).startswith("."):
# #             return 1
# #         return 0
# #     children = get_children(node)
# #     hidden_files_count = list(map(get_hidden_files_count, children))
# #     return sum(hidden_files_count)
# #
# # # Решение учителя
# # def get_hidden_files_count(node):
# #     name = get_name(node)
# #     if is_file(node):
# #         return name.startswith('.')
# #     children = get_children(node)
# #     hidden_files_count = list(map(get_hidden_files_count, children))
# #     return sum(hidden_files_count)
#
# def get_subdirectories_info(node):
#     children = fs.get_children(node)
#     # Нас интересуют только директории
#     filtered = filter(fs.is_directory, children)
#     # Запускаем подсчет для каждой директории
#     result = map(
#         lambda child: (fs.get_name(child), get_files_count(child)),
#         filtered,
#     )
#     return list(result)
#
# def get_size(node):
#     if is_file(node):
#         return get_meta(node)['size']
#
#     children = get_children(node)
#     sizes = map(get_size, children)
#     return sum(sizes)
#
#
# def du(directory):
#     children = get_children(directory)
#
#     result = list(map(
#         lambda child: (get_name(child), get_size(child)),
#         children,
#     ))
#
#     result.sort(key=lambda item: item[1], reverse=True)
#     return result
#
#
# import os
#
#
# def find_empty_dir_paths(tree):
#     # Аккумулятором выступает ancestry, путь от корня до текущего узла
#     def walk(node, ancestry):
#         name = fs.get_name(node)
#         # Путь до текущего узла это путь до родителя плюс имя узла
#         new_ancestry = os.path.join(ancestry, name)
#         children = fs.get_children(node)
#         if len(children) == 0:
#             return new_ancestry
#         dir_paths = filter(fs.is_directory, children)
#         # Каждый потомок получает путь до своего родителя
#         output = list(map(lambda child: walk(child, new_ancestry), dir_paths))
#         return fs.flatten(output)
#
#     # Корень называется "/", и os.path.join("", "/") даёт "/"
#     return walk(tree, "")
#
#
# print(find_empty_dir_paths(tree))
# # => ['/etc/apache', '/etc/consul/data', '/logs']

# class PasswordValidator():
#     OPTIONS = {
#         'min_len': 8,
#         'contain_numbers': False,
#     }
#
#     # BEGIN (write your solution here)
#
#     def __init__(self, **options):
#         self.options = {
#             key: options.get(key, value)
#             for key, value in self.OPTIONS.items()
#         }
#
#     def _has_number(self, password):
#
#         return any(char.isdigit() for char in password)
#
#     def validate(self, password):
#         result = {}
#         print(self.options)
#         if len(password) < self.options['min_len']:
#             result['min_len'] = 'too small'
#
#         if self.options['contain_numbers'] and not self._has_number(password):
#             result['contain_numbers'] = 'should contain at least one number'
#
#         print(result)
#
#         return result
#
# # strict = PasswordValidator(min_len=4, contain_numbers=True)
# # default = PasswordValidator()
# # long = PasswordValidator(min_len=12)
# #
# # assert strict.validate("abcd") == {
# #     "contain_numbers": "should contain at least one number"
# # }
#
#
# validator = PasswordValidator(contain_numberz=None)
# errors1 = validator.validate("qwertya3sdf")
# print(errors1)
# assert not errors1
# assert PasswordValidator.OPTIONS == {"min_len": 8, "contain_numbers": False}


# from urllib.parse import urlparse, parse_qs
#
#
# class Url:
#     def __init__(self, url):
#         self.url = url
#         self.hostname = urlparse(url).hostname
#         self.scheme = urlparse(url).scheme
#         self.port = urlparse(url).port
#         self.query = parse_qs(urlparse(url).query)
#
#     def get_scheme(self):
#         return self.scheme
#
#     def get_hostname(self):
#         return self.hostname
#
#     def get_query_params(self):
#         return self.query
#
#     def get_query_param(self, name, default=None):
#         if name in self.query:
#             return self.query[name][0]
#         return default
#
#     def __eq__(self, other):
#         return self.url == other.url
#
#
# URL1 = "http://hexlet.io?key=value&key2=value2"
# URL2 = "https://google.com:80?a=b&c=d&lala=value"
#
#
# url = Url(URL1)
# print(url.get_query_params())
# print(url.get_query_param("key"))
#
#
#
# def test_url1():
#     url = Url(URL1)
#     assert url.get_scheme() == "http"
#     assert url.get_hostname() == "hexlet.io"
#     assert url.get_query_params() == {
#         "key": ["value"],
#         "key2": ["value2"],
#     }
#     assert url.get_query_param("key") == "value"
#     assert url.get_query_param("key2", "lala") == "value2"
#     assert url.get_query_param("new", "ehu") == "ehu"
#     assert url == (Url(URL1))
#     assert not url == (Url(URL2))

from functools import reduce as _reduce


class Collection:
    def __init__(self, iterable):
        self.iterable = iterable

    def map_(self, func):
        return Collection(list(map(func, self.iterable)))

    def filter_(self, func):
        return Collection(list(filter(func, self.iterable)))

    def reduce_(self, func, acc=None):
        return Collection([_reduce(func, self.iterable, acc)])

    # возвращает коллекцию с уникальными значениями
    def unique(self):
        tuples = set(tuple(sorted(d.items())) for d in self.iterable)
        return Collection(list(dict(t) for t in tuples))

    # группирует коллекцию по указаному ключу
    def group_by(self, func):
        def reducer(acc, val):
            key, value = func(val)
            if key not in acc:
                acc[key] = []
            acc[key].append(value)
            return acc
        result_dict = _reduce(reducer, self.iterable, {})
        return Collection([{k: v} for k, v in result_dict.items()])

    # сортирует колекцию по ключу
    def sort_by(self, func):
        return Collection(sorted(self.iterable, key=func))

    def print(self):
        print(self.iterable)
        return Collection(self.iterable)

    def all(self):
        return list(self.iterable)


raw = [
    {"name": "istambul", "country": "turkey"},
    {"name": "Moscow ", "country": " Russia"},
    {"name": "iStambul", "country": "tUrkey"},
    {"name": "antalia", "country": "turkeY "},
    {"name": "samarA", "country": "  ruSsiA"},
]

def format(cities):
    def normalize(city):
        return {
            "name": city["name"].strip().lower(),
            "country": city["country"].strip().lower(),
        }

    return (
        Collection(cities)
        .map_(normalize)
        .unique()
        .sort_by(lambda city: city["name"])
        .group_by(lambda city: (city["country"], city["name"]))
        .sort_by(lambda item: list(item.keys()))
        .all()
    )

print(format(raw))



