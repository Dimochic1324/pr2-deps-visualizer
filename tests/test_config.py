import sys

import pytest

sys.path.append("src")

from config import read_config, check_config

EXPECTED_DEPTH = 3


def test_read_config():
    config = read_config("config.json")

    assert config["package"] == "requests"
    assert config["max_depth"] == EXPECTED_DEPTH


def test_config_not_found():
    with pytest.raises(ValueError):
        read_config("nothing.json")


def test_wrong_json():
    with pytest.raises(ValueError):
        read_config("configs/error_json.json")


def test_good_config():
    config = read_config("config.json")

    check_config(config)


def test_wrong_depth():
    config = read_config("configs/error_depth.json")

    with pytest.raises(ValueError):
        check_config(config)


def test_no_package():
    config = read_config("configs/error_no_package.json")

    with pytest.raises(ValueError):
        check_config(config)
