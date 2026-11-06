"""Small helpers for cleaning up lists."""


#hellooo my name is nikhil pandey 

def remove_blank_strings(items: list[str]) -> list[str]:
    """Return a new list without empty or whitespace-only strings.

    Strings that contain any non-whitespace character are kept unchanged,
    including their surrounding whitespace.

    Args:
        items: The strings to filter. It is not modified.

    Hey my name is nikhil pandeyyyy
    """
    return [s for s in items if s.strip()]
