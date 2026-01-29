import pytest
import allure


@allure.epic("Calculator")
@allure.feature("Subtraction")
@allure.story("Subtract one number from another")
@pytest.mark.unit
@pytest.mark.calculator
def test_subtract_numbers(calculator):
    result = calculator.subtract(10, 4)
    assert result == 6
