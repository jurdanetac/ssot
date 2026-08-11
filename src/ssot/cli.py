#!/usr/bin/env python3

import re
import sys
import tomllib

from pathlib import Path

BRACKET_PLACEHOLDER_RE = re.compile(r"\[\[ (.*?) \]\]")
TPL_FILE_RE = re.compile(r"(.*\.tpl)", re.IGNORECASE)

def main(args):
    ssot_file = args[0]
    ssot_dictionary = None
    
    # Load dictionary from SSoT
    with open(ssot_file, "rb") as f:
        ssot_dictionary = tomllib.load(f)

    target = Path(args[1]).resolve()
    if target.is_dir():
        templates = [f for f in target.iterdir() if TPL_FILE_RE.match(f.suffix)]
        if templates:
            print("FOUND:")
            for tpl in templates:
                print(tpl)
    elif target.is_file():
        print("file")
    else:
        print(f"Target '{target}' neither directory nor file.")
        sys.exit(1)

    
if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print("USAGE: python3 ssot.toml target")
        sys.exit(1)

    main(args)
