@echo off
chcp 65001 >nul

echo TEST 1 - прямые зависимости requests
python src/main.py --config config.json

echo.

echo TEST 2 - прямые зависимости flask
python src/main.py --config configs/flask.json

echo.

echo TEST 3 - несуществующий пакет
python src/main.py --config configs/unknown_package.json

echo.

echo TEST 4 - неверный адрес репозитория
python src/main.py --config configs/wrong_url.json

pause
