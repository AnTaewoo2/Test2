from slugify import slugify


def test_slugify_lowercases_and_hyphenates():
    assert slugify("Hello World") == "hello-world"


def test_slugify_handles_multiple_words():
    assert slugify("A quick brown fox") == "a-quick-brown-fox"


def test_slugify_collapses_and_trims_whitespace():
    assert slugify("  Hello   World  ") == "hello-world"


def test_slugify_empty_and_whitespace_only():
    assert slugify("") == ""
    assert slugify("   ") == ""


def test_slugify_preserves_lowercased_unicode_text():
    assert slugify("Café Déjà Vu") == "café-déjà-vu"


def test_slugify_handles_punctuation():
    assert slugify("Hello, World!") == "hello,-world!"

