# wordfreq

Count case-insensitive word frequencies in a UTF-8 text file and write the result as JSON.

## Requirements

Python 3.9 or newer (the script uses built-in generic annotations such as `dict[str, object]`). No third-party packages. Verified on Python 3.11.

## Usage

```
python3 count_words.py INPUT [-o OUTPUT]
```

| Argument | Required | Description |
| --- | --- | --- |
| `input` | yes | Path to the UTF-8 text file to read. |
| `-o`, `--output` | no | Path of the JSON file to write. Defaults to `<input>.wordfreq.json`. |

On Windows, use `python` or `py -3` in place of `python3`.

## Example

Run from the repository root:

```
python3 tools/wordfreq/count_words.py tools/wordfreq/sample.txt
```

This writes `tools/wordfreq/sample.txt.wordfreq.json`. To choose the output path explicitly:

```
python3 tools/wordfreq/count_words.py tools/wordfreq/sample.txt -o counts.json
```

## Output format

```json
{
  "source": "tools/wordfreq/sample.txt",
  "total_words": 27,
  "unique_words": 23,
  "counts": {
    "easy": 2,
    "small": 2,
    "a": 1,
    "and": 1
  }
}
```

| Field | Description |
| --- | --- |
| `source` | The input path exactly as passed on the command line. |
| `total_words` | Total number of word occurrences. |
| `unique_words` | Number of distinct words. |
| `counts` | Maps each word to its count, ordered by count descending, then alphabetically. |

A word is a run of letters (`[^\W\d_]+`), so digits and underscores never form part of one. Matching is case-insensitive, so `Small` and `small` are counted together.
