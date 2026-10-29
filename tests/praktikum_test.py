from praktikum.praktikum import main


class TestPraktikumMain:
    """Тесты для функции main()."""

    def test_main_prints_bun(self, capsys):
        main()
        assert "(==== black bun ====)" in capsys.readouterr().out

    def test_main_prints_sour_cream(self, capsys):
        main()
        assert "= sauce sour cream =" in capsys.readouterr().out

    def test_main_prints_cutlet(self, capsys):
        main()
        assert "= filling cutlet =" in capsys.readouterr().out

    def test_main_prints_dinosaur(self, capsys):
        main()
        assert "= filling dinosaur =" in capsys.readouterr().out

    def test_main_does_not_print_sausage(self, capsys):
        main()
        assert "= filling sausage =" not in capsys.readouterr().out

    def test_main_prints_price(self, capsys):
        main()
        assert "Price: 700" in capsys.readouterr().out