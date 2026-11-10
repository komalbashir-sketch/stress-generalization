#!/usr/bin/env python3
"""Remove raw social-media text from prediction CSVs while preserving audit linkage."""

import argparse
import hashlib
import re
from pathlib import Path
import pandas as pd

def normalize_text(text):
    if pd.isna(text):
        return ""
    text = str(text).lower().strip()
    text = re.sub(r"https?://\S+|www\.\S+", "<url>", text)
    text = re.sub(r"\s+", " ", text)
    return text

def text_hash(text):
    return hashlib.sha256(normalize_text(text).encode("utf-8")).hexdigest()

def sanitize_csv(src: Path, dst: Path):
    df = pd.read_csv(src)
    if "text" in df.columns:
        df.insert(0, "text_hash", df["text"].map(text_hash))
        df = df.drop(columns=["text"])
    dst.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(dst, index=False)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="CSV file or directory containing CSV files")
    p.add_argument("output", help="Output CSV file or directory")
    args = p.parse_args()

    src = Path(args.input)
    dst = Path(args.output)

    if src.is_file():
        sanitize_csv(src, dst)
    else:
        dst.mkdir(parents=True, exist_ok=True)
        for f in src.rglob("*.csv"):
            sanitize_csv(f, dst / f.relative_to(src))

if __name__ == "__main__":
    main()
