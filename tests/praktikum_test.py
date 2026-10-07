from praktikum.praktikum import main


class TestPraktikumMain:
    """Тесты для функции main()."""

    def test_main_runs_and_prints_receipt(self, capsys):
        """main() выполняется без ошибок и печатает чек."""
        main()

        captured = capsys.readouterr()
        output = captured.out

        # Булочка выбрана верно
        assert "(==== black bun ====)" in output
        # Добавленные соус и начинки в чеке
        assert "= sauce sour cream =" in output
        assert "= filling cutlet =" in output
        assert "= filling dinosaur =" in output
        # Удалённый ингредиент отсутствует
        assert "= filling sausage =" not in output
        # Итоговая цена
        assert "Price: 700" in output