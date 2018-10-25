from src.cunao import get_quotes, write_quote_to_slack
from mock import patch


def test_get_quotes():
    quotes = get_quotes()
    assert quotes == [{'Quote': 'Con una cerveza no das positivo'}]


def test_write_quote_to_slack():
    with patch('src.cunao.requests.post') as mock_get:
        write_quote_to_slack('test quote')
        assert mock_get.called
