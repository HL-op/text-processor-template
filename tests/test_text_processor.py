import pytest
from text_processor import TextProcessor

@pytest.fixture
def processor():
    return TextProcessor()

# Test word_count function
def test_word_count(processor):
    # Test English text
    assert processor.word_count("Hello world") == 2
    # Test Chinese text
    assert processor.word_count("你好 世界") == 2
    # Test mixed text
    assert processor.word_count("Hello 世界") == 2
    # Test empty text
    assert processor.word_count("") == 0

# Test char_frequency function
def test_char_frequency(processor):
    text = "hello world"
    result = processor.char_frequency(text)
    assert len(result) <= 5
    # Check if result is a list of tuples
    assert all(isinstance(item, tuple) for item in result)

# Test sentiment_analysis function
def test_sentiment_analysis(processor):
    # Test positive sentiment
    assert processor.sentiment_analysis("I love this") in ["positive", "neutral"]
    # Test negative sentiment
    assert processor.sentiment_analysis("I hate this") in ["negative", "neutral"]
    # Test neutral sentiment
    assert processor.sentiment_analysis("This is a test") == "neutral"

# Test text_summary function
def test_text_summary(processor):
    text = "This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence."
    # Test default n=3
    summary = processor.text_summary(text)
    assert len(summary.split('.')) == 4  # Including empty string at end
    # Test custom n=2
    summary = processor.text_summary(text, n=2)
    assert len(summary.split('.')) == 3  # Including empty string at end
    # Test empty text
    assert processor.text_summary("") == ""

# Test edge cases
def test_edge_cases(processor):
    # Test very long text
    long_text = "Hello " * 1000
    assert processor.word_count(long_text) == 1000
    # Test text with special characters
    assert processor.word_count("Hello, world!") == 2
    # Test text with multiple spaces
    assert processor.word_count("Hello   world") == 2