import settings
from src.cunao import get_quotes, write_quote_to_slack
from mock import call, patch

TEST_QUOTE = 'Con una cerveza no das positivo'


def test_get_quotes():
    quotes = get_quotes()
    assert quotes == [{'Quote': TEST_QUOTE}]


def test_write_quote_to_slack():
    with patch('src.cunao.requests.post') as mock_get:
        write_quote_to_slack(TEST_QUOTE)
        assert mock_get.called


def test_write_quote_to_slack_with_more_tha_one_url():
    """
    Check if the quote is sent to all the slack urls provided
    """
    settings.SLACK_URLS = ['http://www.url1.com', 'http://www.url2.com']
    expected_calls = [call('http://www.url1.com', json={'text': TEST_QUOTE.upper()}),
                      call('http://www.url2.com', json={'text': TEST_QUOTE.upper()})]

    with patch('src.cunao.requests.post') as mock_get:
        write_quote_to_slack(TEST_QUOTE)

        assert mock_get.call_count is len(expected_calls)
        mock_get.assert_has_calls(expected_calls, any_order=True)
