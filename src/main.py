from config import parse_arguments, read_config, check_config
from graph import read_test_repository, build_graph


def print_graph(graph, cycles):
    print("Граф зависимостей:")

    for package, dependencies in graph.items():
        if dependencies:
            print(package, "->", ", ".join(dependencies))
        else:
            print(package, "-> нет зависимостей")

    for cycle in cycles:
        print("Найден цикл:", " -> ".join(cycle))


def main():
    args = parse_arguments()

    try:
        config = read_config(args.config)
        check_config(config)

        test_repository = {}

        if config["test_mode"]:
            test_repository = read_test_repository(config["repository"])

            if config["package"] not in test_repository:
                raise ValueError(
                    f"пакет не найден в репозитории: {config['package']}"
                )

        graph, cycles = build_graph(config, test_repository)

    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    print_graph(graph, cycles)


if __name__ == "__main__":
    main()
