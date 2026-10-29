import pytest
from unittest.mock import Mock


class TestBurger:
    """Тесты для класса Burger."""

    def test_init_bun_is_none(self, burger):
        """При создании бургер не содержит булочки."""
        assert burger.bun is None

    def test_init_ingredients_is_empty(self, burger):
        """При создании бургер не содержит ингредиентов."""
        assert burger.ingredients == []

    def test_set_buns(self, burger, mock_bun):
        """Булочка устанавливается корректно."""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_set_buns_replaces_previous(self, burger, mock_bun):
        """Повторная установка булочки заменяет предыдущую."""
        new_bun = Mock()
        burger.set_buns(mock_bun)
        burger.set_buns(new_bun)
        assert burger.bun == new_bun

    def test_add_ingredient_increases_length(self, burger, mock_ingredient):
        """Добавление ингредиента увеличивает длину списка."""
        ing = mock_ingredient()
        burger.add_ingredient(ing)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_correct_object(self, burger, mock_ingredient):
        """В список добавляется именно тот ингредиент."""
        ing = mock_ingredient()
        burger.add_ingredient(ing)
        assert burger.ingredients[0] == ing

    def test_add_multiple_ingredients(self, burger, mock_ingredient):
        """Несколько ингредиентов добавляются по порядку."""
        ing1 = mock_ingredient(name="cutlet", price=200.0)
        ing2 = mock_ingredient(name="hot sauce", price=50.0, ing_type="SAUCE")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        assert burger.ingredients == [ing1, ing2]

    def test_remove_ingredient(self, burger, mock_ingredient):
        """Удаление ингредиента по индексу."""
        ing1 = mock_ingredient(name="cutlet")
        ing2 = mock_ingredient(name="hot sauce")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.remove_ingredient(0)

        assert burger.ingredients == [ing2]

    def test_remove_ingredient_last(self, burger, mock_ingredient):
        """Удаление последнего ингредиента."""
        ing = mock_ingredient()
        burger.add_ingredient(ing)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_forward(self, burger, mock_ingredient):
        """Перемещение ингредиента с 0-й позиции на 1-ю."""
        ing1 = mock_ingredient(name="cutlet")
        ing2 = mock_ingredient(name="hot sauce")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [ing2, ing1]

    def test_move_ingredient_backward(self, burger, mock_ingredient):
        """Перемещение ингредиента с последней позиции в начало."""
        ing1 = mock_ingredient(name="cutlet")
        ing2 = mock_ingredient(name="hot sauce")
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ing2, ing1]

    def test_get_price_with_bun_and_no_ingredients(self, burger, mock_bun):
        """Цена = цена булочки * 2, если нет ингредиентов."""
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    @pytest.mark.parametrize(
        "ingredient_prices, expected_extra",
        [
            ([], 0.0),
            ([50.0], 50.0),
            ([50.0, 30.0], 80.0),
            ([10.0, 20.0, 30.0], 60.0),
        ],
    )
    def test_get_price_parameterized(
        self, burger, mock_bun, mock_ingredient, ingredient_prices, expected_extra
    ):
        """Цена = булочки*2 + сумма цен ингредиентов."""
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            burger.add_ingredient(mock_ingredient(price=price))

        assert burger.get_price() == 200.0 + expected_extra

    # --- Разделенные тесты для чека БЕЗ ингредиентов (4 строки) ---

    def test_receipt_without_ingredients_top_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        lines = burger.get_receipt().split("\n")
        assert lines[0] == "(==== black bun ====)"

    def test_receipt_without_ingredients_bottom_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        lines = burger.get_receipt().split("\n")
        assert lines[1] == "(==== black bun ====)"

    def test_receipt_without_ingredients_empty_line(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        lines = burger.get_receipt().split("\n")
        assert lines[2] == ""

    def test_receipt_without_ingredients_price(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        lines = burger.get_receipt().split("\n")
        assert lines[3] == "Price: 200.0"

    # --- Разделенные тесты для чека С ОДНИМ ингредиентом (5 строк) ---

    def test_receipt_with_one_ingredient_top_bun(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient(name="cutlet", price=200.0, ing_type="FILLING"))
        lines = burger.get_receipt().split("\n")
        assert lines[0] == "(==== black bun ====)"

    def test_receipt_with_one_ingredient_content(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient(name="hot sauce", price=50.0, ing_type="SAUCE"))
        lines = burger.get_receipt().split("\n")
        assert lines[1] == "= sauce hot sauce ="

    def test_receipt_with_one_ingredient_bottom_bun(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient(name="cutlet", price=200.0))
        lines = burger.get_receipt().split("\n")
        assert lines[2] == "(==== black bun ====)"

    def test_receipt_with_one_ingredient_empty_line(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient(name="cutlet", price=200.0))
        lines = burger.get_receipt().split("\n")
        assert lines[3] == ""

    def test_receipt_with_one_ingredient_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient(price=250.0))
        lines = burger.get_receipt().split("\n")
        assert lines[4] == "Price: 450.0"

    # --- Разделенные тесты для проверки вызовов моков ---

    def test_get_receipt_calls_bun_name_twice(self, burger, mock_bun):
        """Проверка, что get_name() булочки вызывается дважды."""
        burger.set_buns(mock_bun)
        burger.get_receipt()
        assert mock_bun.get_name.call_count == 2

    def test_receipt_calls_ingredient_get_type(self, burger, mock_bun, mock_ingredient):
        ing = mock_ingredient()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ing)
        burger.get_receipt()
        ing.get_type.assert_called_once()

    def test_receipt_calls_ingredient_get_name(self, burger, mock_bun, mock_ingredient):
        ing = mock_ingredient()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ing)
        burger.get_receipt()
        ing.get_name.assert_called_once()

    def test_receipt_calls_ingredient_get_price(self, burger, mock_bun, mock_ingredient):
        ing = mock_ingredient()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ing)
        burger.get_receipt()
        ing.get_price.assert_called_once()