import sys

import pytest

sys.path.append("src")

from graph import read_test_repository, build_graph


def make_config(repository, max_depth=10, filter_text=""):
    return {
        "package": "A",
        "repository": repository,
        "test_mode": True,
        "max_depth": max_depth,
        "filter": filter_text
    }


def build(repository, max_depth=10, filter_text=""):
    config = make_config(repository, max_depth, filter_text)
    test_repository = read_test_repository(repository)
    return build_graph(config, test_repository)


def test_read_repository():
    repository = read_test_repository("repos/simple.txt")

    assert repository["A"] == ["B", "C"]
    assert repository["D"] == []


def test_simple_graph():
    graph, cycles = build("repos/simple.txt")

    assert set(graph) == {"A", "B", "C", "D", "E"}
    assert cycles == []


def test_cycle():
    graph, cycles = build("repos/cycle.txt")

    assert cycles == [["A", "B", "C", "A"]]


def test_max_depth():
    graph, cycles = build("repos/deep.txt", max_depth=3)

    assert list(graph) == ["A", "B", "C"]


def test_filter():
    graph, cycles = build("repos/filter.txt", filter_text="TEST")

    assert "TEST" not in graph
    assert graph["A"] == ["B"]


def test_bad_names():
    with pytest.raises(ValueError):
        read_test_repository("repos/bad_names.txt")
