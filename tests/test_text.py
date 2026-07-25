from aungko1990 import normalize_title, slugify


def test_normalize_title_collapses_extra_whitespace():
    assert normalize_title("  Aungko1990   Work\nProject  ") == "Aungko1990 Work Project"


def test_slugify_normalizes_case_accents_and_punctuation():
    assert slugify("  Café Guide: Aungko1990 Work!  ") == "cafe-guide-aungko1990-work"


def test_slugify_returns_empty_string_for_blank_input():
    assert slugify(" \t\n ") == ""
