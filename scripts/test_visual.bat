@echo off
chcp 65001 >nul

echo TEST 1 - тестовый граф
python src/main.py --config configs/test_simple.json

echo.

echo TEST 2 - тестовый граф с циклом
python src/main.py --config configs/test_cycle.json

echo.

echo TEST 3 - пакет requests
python src/main.py --config config.json

echo.

echo TEST 4 - пакет flask
python src/main.py --config configs/flask.json

echo.

echo TEST 5 - пакет matplotlib
python src/main.py --config configs/matplotlib.json

pause
