import private


def test_exports() -> None:
    assert private.__all__ == ["foo"]
