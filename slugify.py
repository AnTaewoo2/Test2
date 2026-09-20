import unicodedata


def slugify(text):
    """Lowercase text, collapse whitespace, and remove punctuation."""
    text = text.lower()
    text = "".join(
        character
        for character in text
        if not unicodedata.category(character).startswith("P")
    )
    return "-".join(text.split())


