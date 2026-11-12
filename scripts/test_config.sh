#!/bin/bash

echo TEST 1 - правильный config
python3 src/main.py --config config.json

echo

echo TEST 2 - файл не существует
python3 src/main.py --config nothing.json

echo

echo TEST 3 - ошибка в JSON
python3 src/main.py --config configs/error_json.json

echo

echo TEST 4 - нет параметра package
python3 src/main.py --config configs/error_no_package.json

echo

echo TEST 5 - пустое имя пакета
python3 src/main.py --config configs/error_package.json

echo

echo TEST 6 - пустой репозиторий
python3 src/main.py --config configs/error_repository.json

echo

echo TEST 7 - неверный test_mode
python3 src/main.py --config configs/error_test_mode.json

echo

echo TEST 8 - изображение не png
python3 src/main.py --config configs/error_image.json

echo

echo TEST 9 - неверный ascii_tree
python3 src/main.py --config configs/error_ascii_tree.json

echo

echo TEST 10 - неверная глубина
python3 src/main.py --config configs/error_depth.json

echo

echo TEST 11 - неверный фильтр
python3 src/main.py --config configs/error_filter.json

