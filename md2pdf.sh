#!/bin/bash
set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <file.md> [file2.md ...]"
    exit 1
fi

# OUTDIR="$(dirname "$0")/pdf"
OUTDIR="/mnt/c/data/pdf"

mkdir -p "$OUTDIR"

for input in "$@"; do
    basename="${input%.md}"
    basename="${basename##*/}"
    output="$OUTDIR/${basename}.pdf"
    echo "Converting $input -> $output"
    pandoc "$input" -o "$output" \
        -V mainfont="Noto Sans CJK SC" \
        -V sansfont="Noto Sans CJK SC" \
        -V monofont="Noto Sans Mono CJK SC" \
        -V CJKmainfont="Noto Sans CJK SC" \
        -V CJKoptions="BoldFont=Noto Sans CJK SC Bold" \
        -V geometry:paper=a4paper \
        -V geometry:margin=3cm \
        --pdf-engine xelatex
    echo "Done: $output"
done
