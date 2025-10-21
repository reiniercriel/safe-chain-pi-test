from testpkg import add


def test_add_integers():
    assert add(1, 2) == 3


def test_add_type_error():
    try:
        add(1, "a")
        assert False, "TypeError expected"
    except TypeError as e:
        assert "both arguments" in str(e)
