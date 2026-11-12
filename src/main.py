from config import parse_arguments, read_config, check_config


def main():
    args = parse_arguments()

    try:
        config = read_config(args.config)
        check_config(config)

    except ValueError as error:
        print(f"Ошибка: {error}")
        return

    print("Параметры запуска:")
    for key, value in config.items():
        print(f"{key} = {value}")


if __name__ == "__main__":
    main()
