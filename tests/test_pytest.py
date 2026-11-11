# pip install pytest
# python3 -m pytest
# pip install pytest-cov
# python3 -m pytest --cov --cov-report=html

import pytest

from functions import *


params_first = (
    (5, 'Стоимость доставки: 200 руб.'),
    (10.1, 'Стоимость доставки: 500 руб.'),
    (30, 'Стоимость доставки: 500 руб.'),
)

@pytest.mark.parametrize(
    'weight,expected',
    params_first
)
def test_weight(weight, expected):
    assert get_cost(weight) == expected




params_second = (
    ('Аладдин', 'Мадагаскар', 'Бетховен', 'Мадагаскар'),
    ('Перевозчик', 'Мадагаскар', 'Бетховен 2', 'все фильмы одинаковой длины'),
    ('Перевозчик', 'Мадагаскар', 'Бетховен', 'невозможно выбрать'),
)

@pytest.mark.parametrize(
    'first, second, third, expected',
    params_second
)
def test_film_length(first, second, third, expected):
    assert longest_film(first, second, third) == expected



params_third = (
    ('цветок', 'токцве'),
    ('якорь', 'яоькр'),
)

@pytest.mark.parametrize(
    'word,expected',
    params_third
)
def test_encrypt(word, expected):
    assert encrypt(word) == expected