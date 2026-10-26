def remove_first_level(tree):
    new_tree = []
    for item in tree:
        if isinstance(item, list):
            new_tree.extend(item)
    return new_tree


print (remove_first_level([
        [1, [3, 2]],
        2,
        [3, 5],
        2,
        [130, [1, [550, 10]]],
    ])
)

# python-package  # Директория (метаданные: {'hidden': True})
# ├── Makefile  # Файл
# ├── README.md  # Файл
# ├── dist  # Пустая директория
# ├── tests  # Директория
# │   └── test_solution.py  # Файл
# ├── pyproject.toml  # Файл
# └── .venv  # Директория (метаданные: {'owner': 'root', 'hidden': False})
#     └── lib  # Директория
#         └── python3.6  # Директория
#             └── site-packages  # Директория
#                 └── hexlet-python-package.egg-link  # Файл

def generate():
    return mkdir(
        'python-package',
        [
            mkfile('Makefile'),
            mkfile('README.md'),
            mkdir('dist'),
            mkdir('tests', [
                mkfile('test_solution.py'),
            ]),
            mkfile('pyproject.toml'),
            mkdir(
                '.venv',
                [
                    mkdir('lib', [
                        mkdir('python3.6', [
                            mkdir('site-packages', [
                                mkfile('hexlet-python-package.egg-link'),
                            ]),
                        ]),
                    ]),
                ],
                {'owner': 'root', 'hidden': False},
            ),
        ],
        {'hidden': True},
    )