import argparse
import json


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config",
        default="config.json",
        help="Путь к конфигурационному файлу"
    )

    return parser.parse_args()


def read_config(config_path):
    try:
        with open(config_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise ValueError(
            f"не удалось открыть конфигурационный файл: {config_path}"
        )

    except json.JSONDecodeError:
        raise ValueError(
            f"ошибка чтения JSON-файла: {config_path}"
        )


def check_config(config):
    keys = [
        "package",
        "repository",
        "test_mode",
        "output_image",
        "ascii_tree",
        "max_depth",
        "filter"
    ]

    for key in keys:
        if key not in config:
            raise ValueError(f"не задан параметр {key}")

    if not isinstance(config["package"], str) or config["package"] == "":
        raise ValueError("имя пакета должно быть непустой строкой")

    if not isinstance(config["repository"], str) or config["repository"] == "":
        raise ValueError("репозиторий должен быть непустой строкой")

    if not isinstance(config["test_mode"], bool):
        raise ValueError("test_mode должен быть true или false")

    if not str(config["output_image"]).endswith(".png"):
        raise ValueError("имя изображения должно заканчиваться на .png")

    if not isinstance(config["ascii_tree"], bool):
        raise ValueError("ascii_tree должен быть true или false")

    if type(config["max_depth"]) is not int or config["max_depth"] < 1:
        raise ValueError("max_depth должен быть целым числом больше 0")

    if not isinstance(config["filter"], str):
        raise ValueError("filter должен быть строкой")

    if not isinstance(config.get("reverse_mode", False), bool):
        raise ValueError("reverse_mode должен быть true или false")
