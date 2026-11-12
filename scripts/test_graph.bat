@echo off
chcp 65001 >nul

echo TEST 1 - простой граф
python src/main.py --config configs/test_simple.json

echo.

echo TEST 2 - циклические зависимости
python src/main.py --config configs/test_cycle.json

echo.

echo TEST 3 - максимальная глубина 3
python src/main.py --config configs/test_depth.json

echo.

echo TEST 4 - фильтр TEST
python src/main.py --config configs/test_filter.json

echo.

echo TEST 5 - неверные имена пакетов
python src/main.py --config configs/test_bad_names.json

echo.

echo TEST 6 - файл репозитория не найден
python src/main.py --config configs/test_no_file.json

echo.

echo TEST 7 - пакета нет в репозитории
python src/main.py --config configs/test_no_package.json

echo.

echo TEST 8 - реальный пакет requests
python src/main.py --config config.json

pause
