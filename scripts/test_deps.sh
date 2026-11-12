#!/bin/bash

echo TEST 1 - прямые зависимости requests
python3 src/main.py --config config.json

echo

echo TEST 2 - прямые зависимости flask
python3 src/main.py --config configs/flask.json

echo

echo TEST 3 - несуществующий пакет
python3 src/main.py --config configs/unknown_package.json

echo

echo TEST 4 - неверный адрес репозитория
python3 src/main.py --config configs/wrong_url.json

