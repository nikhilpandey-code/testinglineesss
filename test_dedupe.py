from dedupe import dedupe, remove_blank_strings


def test_empty_list():
    assert dedupe([]) == []
    assert remove_blank_strings([]) == []


def test_all_duplicates():
    assert dedupe([7, 7, 7, 7]) == [7]


def test_mixed_types():
    items = [1, "1", None, 1, "1", None, (1, 2), (1, 2), [3], [3]]
    assert dedupe(items) == [1, "1", None, (1, 2), [3]]


def test_blank_strings():
    items = ["a", "", "   ", "\t\n", "b ", ""]
    assert remove_blank_strings(items) == ["a", "b "]


def test_order_kept():
    items = ["c", "a", "c", "b", "a"]
    assert dedupe(items) == ["c", "a", "b"]
    assert items == ["c", "a", "c", "b", "a"]  # input is not modified
