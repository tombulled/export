import public


def test_exports() -> None:
    assert public.__all__ == ["export", "foo"]
