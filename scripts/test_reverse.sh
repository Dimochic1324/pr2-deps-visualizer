#!/bin/bash

echo TEST 1 - кто зависит от D
python3 src/main.py --config configs/reverse_simple.json

echo

echo TEST 2 - обратные зависимости в графе с циклом
python3 src/main.py --config configs/reverse_cycle.json

echo

echo TEST 3 - обратные зависимости с глубиной 2
python3 src/main.py --config configs/reverse_depth.json

echo

echo TEST 4 - обратные зависимости с фильтром TEST
python3 src/main.py --config configs/reverse_filter.json

echo

echo TEST 5 - от корневого пакета никто не зависит
python3 src/main.py --config configs/reverse_root.json

echo

echo TEST 6 - реальный репозиторий
python3 src/main.py --config configs/reverse_real.json

echo

echo TEST 7 - неверный reverse_mode
python3 src/main.py --config configs/error_reverse_mode.json

