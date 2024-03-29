# Dedup

## Requirements

Text need to be delimited by lines starting with `## START ##` followed by anything that identifies the document, for example source file and URI.

Example:

```
## START ## archive.war https://example.org/
Text text text ...
```

## How to run

1. Create hashes by piping text into `hashes.py`
2. Deduplicate documents / hashes by running `dedup.py`
3. Use result from (2) to extract documents from original text

Example:

```
# ./hashes.py < text.txt > hashes.txt
# ./dedup.py < hashes.txt > urls.txt
# ./extract urls.txt < text.txt > text_deduped.txt 2> text_dups.txt
```
