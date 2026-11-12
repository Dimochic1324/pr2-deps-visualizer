from config import parse_arguments, read_config, check_config
from repository import get_dependencies


def main():
    args = parse_arguments()

    try:
        config = read_config(args.config)
        check_config(config)

        dependencies = get_dependencies(
            config["repository"],
            config["package"]
        )

    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    print(f"Прямые зависимости пакета {config['package']}:")

    if not dependencies:
        print("нет зависимостей")

    for dependency in dependencies:
        print(dependency)


if __name__ == "__main__":
    main()
