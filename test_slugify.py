from slugify import slugify


def test_slugify_lowercases_and_hyphenates():
    assert slugify("Hello World") == "hello-world"


def test_slugify_handles_multiple_words():
    assert slugify("A quick brown fox") == "a-quick-brown-fox"
