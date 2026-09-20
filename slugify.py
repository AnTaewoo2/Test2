def slugify(text):
    """Lowercase text, collapse whitespace, and preserve punctuation."""
    return "-".join(text.lower().split())

