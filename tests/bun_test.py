import pytest

from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun."""

    @pytest.mark.parametrize(
        "name",
        ["black bun", "white bun", "red bun", "", "sesame bun"],
    )
    def test_get_name(self, name):
        """Проверка метода get_name."""
        bun = Bun(name, 100)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [100, 200, 300, 0, 150.5],
    )
    def test_get_price(self, price):
        """Проверка метода get_price."""
        bun = Bun("black bun", price)
        assert bun.get_price() == price