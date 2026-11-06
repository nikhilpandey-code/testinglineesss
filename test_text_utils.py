import pytest

from text_utils import slugify, truncate, word_count


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        ("Hello World", "hello-world"),
        ("  Hello,   World!  ", "hello-world"),
        ("Café au Lait", "cafe-au-lait"),
        ("Top 10 Python Tips", "top-10-python-tips"),
        ("already-a-slug", "already-a-slug"),
        ("!!!", ""),
        ("", ""),
    ],
)
def test_slugify(title, expected):
    assert slugify(title) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("   \n\t ", 0),
        ("hello", 1),
        ("Hello, world! How are you?", 5),
        ("  spaced   out\nacross\tlines  ", 4),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected


def test_truncate_leaves_short_text_unchanged():
    assert truncate("short", 10) == "short"
    assert truncate("exactly10!", 10) == "exactly10!"


def test_truncate_cuts_and_adds_ellipsis_within_limit():
    result = truncate("The quick brown fox", 10)
    assert result == "The qui..."
    assert len(result) == 10


def test_truncate_drops_whitespace_before_ellipsis():
    assert truncate("Hello world", 9) == "Hello..."


def test_truncate_limit_of_three_gives_only_ellipsis():
    assert truncate("abcdef", 3) == "..."


def test_truncate_rejects_limit_below_three():
    with pytest.raises(ValueError):
        truncate("abcdef", 2)
