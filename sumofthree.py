def sum_of_three_arrays(a: list[float], b: list[float], c: list[float]) -> list[float]:
    """Return the element-wise sum of three equal-length lists.

    Raises:
        ValueError: If the three lists are not the same length.
    """
    if not len(a) == len(b) == len(c):
        raise ValueError("all three arrays must have the same length")
    return [x + y + z for x, y, z in zip(a, b, c)]
