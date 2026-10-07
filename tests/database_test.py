import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    """Тесты для класса Database."""

    def test_available_buns(self):
        """Проверка метода available_buns."""
        database = Database()
        buns = database.available_buns()
        
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)
        assert buns[0].get_name() == "black bun"

    def test_available_ingredients(self):
        """Проверка метода available_ingredients."""
        database = Database()
        ingredients = database.available_ingredients()
        
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)
        assert ingredients[0].get_name() == "hot sauce"