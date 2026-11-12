import json
import urllib.error
import urllib.request


def get_package_name(requirement):
    name = ""

    for symbol in requirement:
        if symbol in " ;<>=!~[(":
            break
        name += symbol

    return name.lower().replace("_", "-")


def get_dependencies(repository, package):
    url = f"{repository}/{package}/json"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)

    except urllib.error.HTTPError:
        raise ValueError(f"пакет не найден: {package}")

    except urllib.error.URLError:
        raise ValueError(
            f"не удалось подключиться к репозиторию: {repository}"
        )

    requirements = data["info"]["requires_dist"]

    if requirements is None:
        return []

    dependencies = []

    for requirement in requirements:
        if "extra ==" in requirement:
            continue

        name = get_package_name(requirement)

        if name not in dependencies:
            dependencies.append(name)

    return dependencies
