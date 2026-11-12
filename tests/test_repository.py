import sys

sys.path.append("src")

from repository import get_package_name


def test_simple_name():
    assert get_package_name("idna") == "idna"


def test_name_with_version():
    assert get_package_name("urllib3<3,>=1.21.1") == "urllib3"


def test_name_with_condition():
    assert get_package_name('idna; python_version >= "3.8"') == "idna"


def test_name_with_brackets():
    name = get_package_name("Charset_Normalizer (<4,>=2)")
    assert name == "charset-normalizer"
