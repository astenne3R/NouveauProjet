import py


class TestPy:
    def test_addition(self):
        assert 4 == py.add(2, 2)

    def test_substratcion(self):
        assert 2 == py.substract(4, 2)
