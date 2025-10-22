import pytest
from calculator import Calculator

@pytest.fixture(scope="function")
def calculator():
    """
    Создание нового экземпляра калькулятора перед каждым тестом
    """
    return Calculator()

class TestCalcOperations:
    """
    Тестирование базовых операций калькулятора
    """
    @pytest.mark.parametrize("x, y, result", [
        (1, 2, 3),
        (0, 0, 0),
        (-3, 3, 0),
        (2.5, 1.5, 4.0),
        (-2.5, -2.5, -5.0),
    ])
    def test_addition(self, calculator, x, y, result):
        """
        Проверка метода add()
        """
        outcome = calculator.add(x, y)
        assert outcome == result, f"add({x}, {y}) должно вернуть {result}, а получено {outcome}"

    @pytest.mark.parametrize("x, y, result", [
        (8, 2, 4.0),
        (9, 3, 3.0),
        (-12, 3, -4.0),
        (0, 4, 0.0),
        (7.5, 2.5, 3.0),
    ])
    def test_division(self, calculator, x, y, result):
        """
        Проверка метода divide() при корректных данных
        """
        value = calculator.divide(x, y)
        assert value == result, f"divide({x}, {y}) должно вернуть {result}, получено {value}"

    def test_zero_division_error(self, calculator):
        """Проверка, что при делении на ноль вызывается исключение"""
        with pytest.raises(ZeroDivisionError, match="ноль"):
            calculator.divide(5, 0)


class TestPrimeCheck:
    """
    Тестирование функции проверки простых чисел
    """
    @pytest.mark.parametrize("num, expected", [
        (2, True),
        (3, True),
        (4, False),
        (11, True),
        (15, False),
        (1, False),
        (0, False),
        (-7, False),
        (19, True),
        (25, False),
    ])
    def test_is_prime(self, calculator, num, expected):
        """
        Проверка метода is_prime_number()
        """
        result = calculator.is_prime_number(num)
        assert result == expected, f"is_prime_number({num}) → ожидалось {expected}, получено {result}"
