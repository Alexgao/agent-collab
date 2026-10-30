#!/usr/bin/env python3
"""Count case-insensitive word frequencies in a text file."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path


WORD_PATTERN = re.compile(r"[^\W\d_]+", re.UNICODE)


def count_words(input_path: Path) -> dict[str, object]:
    """Return word-frequency data for *input_path*."""
    text = input_path.read_text(encoding="utf-8")
    words = [match.group(0).casefold() for match in WORD_PATTERN.finditer(text)]
    frequencies = Counter(words)
    sorted_counts = dict(
        sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))
    )

    return {
        "source": str(input_path),
        "total_words": len(words),
        "unique_words": len(frequencies),
        "counts": sorted_counts,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count words in a text file and write the frequencies as JSON."
    )
    parser.add_argument("input", type=Path, help="path to the UTF-8 text file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="output JSON path (default: <input>.wordfreq.json)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = args.output or Path(f"{args.input}.wordfreq.json")
    result = count_words(args.input)
    output_path.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
