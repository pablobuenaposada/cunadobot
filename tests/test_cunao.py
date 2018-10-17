import cunao
from mock import patch


def test_get_phrases():
    phrases = cunao.get_phrases()

    assert phrases == [{'Quote': 'Con una cerveza no das positivo'}]


def test_write_quote_to_slack():
    with patch('cunao.requests.post') as mock_get:
        cunao.write_quote_to_slack('test quote')

        assert mock_get.called is True
