from config import parse_arguments, read_config, check_config
from graph import read_test_repository, build_graph, reverse_repository
from visualize import save_image, print_tree


def print_graph(title, graph, cycles, empty_text="нет зависимостей"):
    print(title)

    for package, dependencies in graph.items():
        if dependencies:
            print(package, "->", ", ".join(dependencies))
        else:
            print(package, "->", empty_text)

    for cycle in cycles:
        print("Найден цикл:", " -> ".join(cycle))


def load_config(config_path):
    config = read_config(config_path)
    check_config(config)

    if config.get("reverse_mode", False) and not config["test_mode"]:
        raise ValueError(
            "обратные зависимости работают только в тестовом режиме"
        )

    return config


def load_test_repository(config):
    if not config["test_mode"]:
        return {}

    repository = read_test_repository(config["repository"])

    if config["package"] not in repository:
        raise ValueError(
            f"пакет не найден в репозитории: {config['package']}"
        )

    if config.get("reverse_mode", False):
        repository = reverse_repository(repository)

    return repository


def print_reverse(config, graph, cycles):
    print_graph(
        "Обратные зависимости (пакет -> кто от него зависит):",
        graph,
        cycles,
        "никто не зависит"
    )

    users = set()
    for dependencies in graph.values():
        users.update(dependencies)
    users.discard(config["package"])

    print(f"От пакета {config['package']} зависят:", end=" ")
    print(", ".join(sorted(users)) or "никто")


def print_result(config, graph, cycles):
    print_graph("Граф зависимостей:", graph, cycles)
    save_image(graph, config["output_image"])

    if config["ascii_tree"]:
        print("Дерево зависимостей:")
        print_tree(graph, config["package"], 0, [])


def main():
    args = parse_arguments()

    try:
        config = load_config(args.config)
        test_repository = load_test_repository(config)
        graph, cycles = build_graph(config, test_repository)

    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    if config.get("reverse_mode", False):
        print_reverse(config, graph, cycles)
    else:
        print_result(config, graph, cycles)


if __name__ == "__main__":
    main()
