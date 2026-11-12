#!/bin/bash

echo TEST 1 - тестовый граф
python3 src/main.py --config configs/test_simple.json

echo

echo TEST 2 - тестовый граф с циклом
python3 src/main.py --config configs/test_cycle.json

echo

echo TEST 3 - пакет requests
python3 src/main.py --config config.json

echo

echo TEST 4 - пакет flask
python3 src/main.py --config configs/flask.json

echo

echo TEST 5 - пакет matplotlib
python3 src/main.py --config configs/matplotlib.json

