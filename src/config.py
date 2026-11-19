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


MIN_DEPTH = 1

REQUIRED_KEYS = [
    "package",
    "repository",
    "test_mode",
    "output_image",
    "ascii_tree",
    "max_depth",
    "filter"
]


def is_non_empty_string(value):
    return isinstance(value, str) and value != ""


def is_bool(value):
    return isinstance(value, bool)


def is_png(value):
    return str(value).endswith(".png")


def is_valid_depth(value):
    return type(value) is int and value >= MIN_DEPTH


def is_string(value):
    return isinstance(value, str)


CHECKS = [
    ("package", is_non_empty_string,
     "имя пакета должно быть непустой строкой"),
    ("repository", is_non_empty_string,
     "репозиторий должен быть непустой строкой"),
    ("test_mode", is_bool, "test_mode должен быть true или false"),
    ("output_image", is_png,
     "имя изображения должно заканчиваться на .png"),
    ("ascii_tree", is_bool, "ascii_tree должен быть true или false"),
    ("max_depth", is_valid_depth,
     "max_depth должен быть целым числом больше 0"),
    ("filter", is_string, "filter должен быть строкой"),
]


def check_config(config):
    for key in REQUIRED_KEYS:
        if key not in config:
            raise ValueError(f"не задан параметр {key}")

    for key, check, message in CHECKS:
        if not check(config[key]):
            raise ValueError(message)

    if not is_bool(config.get("reverse_mode", False)):
        raise ValueError("reverse_mode должен быть true или false")
