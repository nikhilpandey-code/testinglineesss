"""Small helpers for cleaning up lists."""


def dedupe(items: list) -> list:
    """Return a new list with duplicates removed, keeping first-appearance order.

    Items are compared by equality, so values that compare equal (for example
    ``1``, ``1.0`` and ``True``) count as duplicates of each other. Unhashable
    items such as lists and dicts are supported; each one costs a linear scan.

    Args:
        items: The list to dedupe. It is not modified.

    Returns:
        A new list holding the first occurrence of each distinct item.
    """
    seen_hashable: set = set()
    seen_unhashable: list = []
    result: list = []
    for item in items:
        try:
            if item in seen_hashable:
                continue
            seen_hashable.add(item)
        except TypeError:
            if item in seen_unhashable:
                continue
            seen_unhashable.append(item)
        result.append(item)
    return result


def remove_blank_strings(items: list[str]) -> list[str]:
    """Return a new list without empty or whitespace-only strings.

    Strings that contain any non-whitespace character are kept unchanged,
    including their surrounding whitespace.

    Args:
        items: The strings to filter. It is not modified.

    Hey my name is nikhil pandeyyyy
    """
    return [s for s in items if s.strip()]
