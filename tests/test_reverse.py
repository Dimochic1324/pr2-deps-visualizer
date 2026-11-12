import sys

sys.path.append("src")

from graph import read_test_repository, build_graph, reverse_repository


def build_reverse(package, repository_path):
    config = {
        "package": package,
        "test_mode": True,
        "max_depth": 10,
        "filter": ""
    }
    repository = read_test_repository(repository_path)
    return build_graph(config, reverse_repository(repository))


def test_reverse_repository():
    repository = {"A": ["B"], "C": ["B"], "B": []}

    assert reverse_repository(repository)["B"] == ["A", "C"]


def test_who_depends_on_d():
    graph, cycles = build_reverse("D", "repos/simple.txt")

    assert set(graph) == {"A", "B", "C", "D"}
    assert graph["D"] == ["B", "C"]


def test_nobody_depends_on_root():
    graph, cycles = build_reverse("A", "repos/simple.txt")

    assert graph == {"A": []}
