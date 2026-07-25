"""Text normalization helpers used by project documentation examples."""

from __future__ import annotations

import re
import unicodedata

_WHITESPACE_RE = re.compile(r"\s+")
_NON_SLUG_RE = re.compile(r"[^a-z0-9]+")


def normalize_title(value: str) -> str:
    """Return a title with leading, trailing, and repeated whitespace collapsed."""
    return _WHITESPACE_RE.sub(" ", value).strip()


def slugify(value: str) -> str:
    """Convert text to a lowercase ASCII slug separated by single hyphens."""
    normalized = unicodedata.normalize("NFKD", normalize_title(value))
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return _NON_SLUG_RE.sub("-", ascii_text).strip("-")
