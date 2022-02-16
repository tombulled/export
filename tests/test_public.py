import public

def test_exports():
    assert public.__all__ == ['foo', 'visibility']