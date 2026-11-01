import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    """Фикстура для создания экземпляра бургера."""
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура-мок булочки с предустановленными значениями."""
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    """
    Фикстура-фабрика моков ингредиентов.

    Возвращает функцию, которая создаёт мок с заданными параметрами.
    Пример использования: mock_ingredient(name="cutlet", price=200.0)
    """
    def _make_ingredient(name="hot sauce", price=100.0, ing_type="SAUCE"):
        ingredient = Mock()
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        ingredient.get_type.return_value = ing_type
        return ingredient

    return _make_ingredient