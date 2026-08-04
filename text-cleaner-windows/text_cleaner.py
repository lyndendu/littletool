"""Pure text-cleaning rules used by the desktop application."""

from __future__ import annotations

import unicodedata


_CJK_PUNCTUATION_TO_ASCII = str.maketrans(
    {
        "。": ".",
        "、": ",",
        "【": "[",
        "】": "]",
        "〔": "[",
        "〕": "]",
        "《": "<",
        "》": ">",
        "〈": "<",
        "〉": ">",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "「": '"',
        "」": '"',
        "『": '"',
        "』": '"',
        "—": "-",
        "–": "-",
        "―": "-",
        "·": ".",
    }
)


def _is_variation_selector(character: str) -> bool:
    """Return True for Unicode variation selectors, which are invisible."""
    code_point = ord(character)
    return 0xFE00 <= code_point <= 0xFE0F or 0xE0100 <= code_point <= 0xE01EF


def clean_text(text: str) -> str:
    """Normalize and clean text while preserving line-feed positions.

    Processing order:
    1. Normalize CRLF and CR newlines to LF.
    2. Replace every tab with one ASCII space.
    3. Apply Unicode NFKC normalization and common CJK punctuation mapping.
    4. Preserve printable ASCII, letters, numbers, marks, punctuation, spaces,
       and line feeds. Remove invisible controls and non-ASCII Unicode symbols
       such as emoji, decorative marks, currency signs, and math symbols.
    """
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = normalized.replace("\t", " ")
    normalized = unicodedata.normalize("NFKC", normalized)
    normalized = normalized.translate(_CJK_PUNCTUATION_TO_ASCII)

    result: list[str] = []
    for character in normalized:
        if character == "\n":
            result.append(character)
            continue

        if _is_variation_selector(character):
            continue

        code_point = ord(character)
        if 0x20 <= code_point <= 0x7E:
            result.append(character)
            continue

        category = unicodedata.category(character)
        if category[0] in {"L", "M", "N", "P", "Z"}:
            result.append(character)

    return "".join(result)
