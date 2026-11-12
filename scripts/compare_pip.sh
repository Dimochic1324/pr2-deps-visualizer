#!/bin/bash

echo Установка пакетов для сравнения
pip install requests flask matplotlib pipdeptree

echo

echo TEST 1 - requests
pip show requests
pipdeptree -p requests

echo

echo TEST 2 - flask
pip show flask
pipdeptree -p flask

echo

echo TEST 3 - matplotlib
pip show matplotlib
pipdeptree -p matplotlib

