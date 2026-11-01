import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient."""

    @pytest.mark.parametrize(
        "ingredient_type",
        [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING],
    )
    def test_get_type(self, ingredient_type):
        """Проверка метода get_type."""
        ingredient = Ingredient(ingredient_type, "name", 100)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        "name",
        ["hot sauce", "sour cream", "cutlet", "dinosaur", ""],
    )
    def test_get_name(self, name):
        """Проверка метода get_name."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [100, 200.0, 300, 400.5, 0],
    )
    def test_get_price(self, price):
        """Проверка метода get_price."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", price)
        assert ingredient.get_price() == price