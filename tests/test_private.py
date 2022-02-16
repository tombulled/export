import private

def test_exports():
    assert private.__all__ == ['foo']