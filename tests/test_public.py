import public


def test_exports() -> None:
    assert public.__all__ == ["foo", "visibility"]
