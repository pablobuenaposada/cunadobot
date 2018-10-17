import cunao


def test_get_phrases():
    phrases = cunao.get_phrases()
    assert phrases == [{'Quote': 'Con una cerveza no das positivo'}]
