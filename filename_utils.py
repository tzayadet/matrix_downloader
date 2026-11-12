"""Cross-platform filename normalization for downloaded media."""

import re


def sanitize_filename(name: str) -> str:
    """Return a safe, bounded filename component for cross-platform output."""
    cleaned = re.sub(r'[\\/*?:"<>|\x00-\x1f]', "_", str(name))
    cleaned = cleaned.strip().strip(".")
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned or cleaned in {".", ".."}:
        cleaned = "download"
    if cleaned.upper().split(".", 1)[0] in {
        "CON", "PRN", "AUX", "NUL",
        *(f"COM{i}" for i in range(1, 10)),
        *(f"LPT{i}" for i in range(1, 10)),
    }:
        cleaned = f"_{cleaned}"
    return cleaned[:160]
