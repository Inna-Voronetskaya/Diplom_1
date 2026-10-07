from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredientTypes:
    """Тесты для констант типов ингредиентов."""

    def test_ingredient_type_sauce(self):
        assert INGREDIENT_TYPE_SAUCE == 'SAUCE'

    def test_ingredient_type_filling(self):
        assert INGREDIENT_TYPE_FILLING == 'FILLING'