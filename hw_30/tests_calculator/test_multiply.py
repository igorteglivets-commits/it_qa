import pytest
import allure


@allure.epic("Calculator")
@allure.feature("Multiplication")
@allure.story("Multiply two numbers")
@pytest.mark.unit
@pytest.mark.calculator
def test_multiply_numbers(calculator):
    result = calculator.multiply(3, 4)
    assert result == 12
