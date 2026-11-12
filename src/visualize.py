import shutil
import subprocess


def make_d2(graph):
    lines = []

    for package, dependencies in graph.items():
        for name in dependencies:
            lines.append(f'"{package}" -> "{name}"')

    return "\n".join(lines) + "\n"


def save_image(graph, image_path):
    d2_path = image_path.replace(".png", ".d2")

    with open(d2_path, "w", encoding="utf-8") as file:
        file.write(make_d2(graph))

    print("Граф на языке D2 сохранён в файл", d2_path)

    if shutil.which("d2") is None:
        print("Ошибка: программа d2 не установлена, PNG не создан")
        return

    result = subprocess.run(["d2", d2_path, image_path])

    if result.returncode != 0:
        print("Ошибка: d2 не смогла создать изображение")
        return

    print("Изображение графа сохранено в файл", image_path)


def print_tree(graph, package, level, path):
    if level == 0:
        line = package
    else:
        line = "    " * (level - 1) + "|-- " + package

    if package in path:
        print(line + " (цикл)")
        return

    print(line)

    for name in graph.get(package, []):
        print_tree(graph, name, level + 1, path + [package])
