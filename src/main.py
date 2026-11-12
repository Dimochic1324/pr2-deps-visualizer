from config import parse_arguments, read_config, check_config
from graph import read_test_repository, build_graph, reverse_repository


def print_graph(title, graph, cycles, empty_text="нет зависимостей"):
    print(title)

    for package, dependencies in graph.items():
        if dependencies:
            print(package, "->", ", ".join(dependencies))
        else:
            print(package, "->", empty_text)

    for cycle in cycles:
        print("Найден цикл:", " -> ".join(cycle))


def main():
    args = parse_arguments()

    try:
        config = read_config(args.config)
        check_config(config)

        reverse_mode = config.get("reverse_mode", False)

        if reverse_mode and not config["test_mode"]:
            raise ValueError(
                "обратные зависимости работают только в тестовом режиме"
            )

        test_repository = {}

        if config["test_mode"]:
            test_repository = read_test_repository(config["repository"])

            if config["package"] not in test_repository:
                raise ValueError(
                    f"пакет не найден в репозитории: {config['package']}"
                )

        if reverse_mode:
            test_repository = reverse_repository(test_repository)

        graph, cycles = build_graph(config, test_repository)

    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    if reverse_mode:
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
    else:
        print_graph("Граф зависимостей:", graph, cycles)


if __name__ == "__main__":
    main()
