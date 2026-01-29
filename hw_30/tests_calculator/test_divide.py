import pytest
import allure


@allure.epic("Calculator")
@allure.feature("Division")
@allure.story("Divide two numbers")
@pytest.mark.unit
@pytest.mark.calculator
def test_divide_numbers(calculator):
    result = calculator.divide(10, 2)
    assert result == 5


@allure.story("Division by zero")
@pytest.mark.unit
@pytest.mark.calculator
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
