import sys

sys.path.append("src")

from visualize import make_d2


def test_d2_edges():
    graph = {"A": ["B", "C"], "B": [], "C": []}
    text = make_d2(graph)

    assert '"A" -> "B"' in text
    assert '"A" -> "C"' in text


def test_d2_cycle():
    graph = {"A": ["B"], "B": ["A"]}
    text = make_d2(graph)

    assert '"B" -> "A"' in text
