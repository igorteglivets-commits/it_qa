import pytest
import allure


@allure.epic("Calculator")
@allure.feature("Addition")
@allure.story("Add two positive numbers")
@pytest.mark.unit
@pytest.mark.calculator
def test_add_two_numbers(calculator):
    result = calculator.add(2, 3)
    assert result == 5
