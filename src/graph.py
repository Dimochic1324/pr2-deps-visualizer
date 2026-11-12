from repository import get_dependencies


def read_test_repository(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

    except FileNotFoundError:
        raise ValueError(f"файл тестового репозитория не найден: {path}")

    repository = {}

    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if ":" not in line:
            raise ValueError(f"неверная строка в репозитории: {line}")

        package, dependencies = line.split(":", 1)
        package = package.strip()
        dependencies = dependencies.split()

        for name in [package] + dependencies:
            if not name.isalpha() or not name.isupper():
                raise ValueError(f"неверное имя пакета: {name}")

        repository[package] = dependencies

    return repository


def get_package_dependencies(package, config, test_repository):
    if config["test_mode"]:
        return test_repository.get(package, [])

    return get_dependencies(config["repository"], package)


def build_graph(config, test_repository):
    graph = {}
    cycles = []

    def dfs(package, depth, path):
        if package in path:
            start = path.index(package)
            cycles.append(path[start:] + [package])
            return

        if package in graph or depth >= config["max_depth"]:
            return

        dependencies = []

        for name in get_package_dependencies(package, config, test_repository):
            if config["filter"] != "" and config["filter"] in name:
                continue
            dependencies.append(name)

        graph[package] = dependencies

        for name in dependencies:
            dfs(name, depth + 1, path + [package])

    dfs(config["package"], 0, [])

    return graph, cycles
