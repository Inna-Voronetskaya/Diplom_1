from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    """Тесты для класса Database."""

    def test_available_buns_count(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_buns_is_bun_object(self):
        database = Database()
        assert isinstance(database.available_buns()[0], Bun)

    def test_available_buns_first_name(self):
        database = Database()
        assert database.available_buns()[0].get_name() == "black bun"

    def test_available_ingredients_count(self):
        database = Database()
        assert len(database.available_ingredients()) == 6

    def test_available_ingredients_is_ingredient_object(self):
        database = Database()
        assert isinstance(database.available_ingredients()[0], Ingredient)

    def test_available_ingredients_first_name(self):
        database = Database()
        assert database.available_ingredients()[0].get_name() == "hot sauce"