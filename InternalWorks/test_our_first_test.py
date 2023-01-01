import pytest

import os
import sys


def test_our_first_test() -> None:
    assert 1 == 1
    numbers = [1, 2, 3]
    fruits_names = ["apple", "orange"]
    if "orange" not in fruits_names:
        fruits_names.append("orange")
    assert sum(numbers) == 6
    assert fruits_names.__contains__("orange")


@pytest.mark.skipif(sys.version_info > (3, 8), reason=str("if condition matched skip it"))
def test_second_test() -> None:
    pass


@pytest.mark.xfail
def test_third_test() -> None:
    assert 1 == 1


@pytest.mark.slow
def test_slow_test() -> None:
    assert 1 == 1


@pytest.mark.slow
def test_slow_test2() -> None:
    pass




class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"{self.name}"


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    print(f"my fruit is {my_fruit}")
    assert my_fruit in fruit_basket


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "company_name",
    ['TikTok', 'Google'],
    ids=['TikTokTest', 'GoogleTest']
)

def test_parametrized_company(company_name: str) -> None:
    print(f"Test with  {company_name}")


def raise_covid_exception()-> None:
    raise ValueError("CoronaVirus Exception")

def test_raise_covid_exception()->None:
    with pytest.raises(ValueError)as e:
        raise_covid_exception()
    assert "CoronaVirus Exception" == str(e.value)