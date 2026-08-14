#!/usr/bin/env python3

import copy
import re
import sys
import tomllib

from pathlib import Path

BRACKET_PLACEHOLDER_RE = re.compile(r"\[\[ (.*?) \]\]")
TPL_FILE_RE = re.compile(r"(.*\.tpl)", re.IGNORECASE)


class DotDict(dict):
    def __getattr__(self, name):
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError(name)

        return self[name]

    def get_dot(self, dot):
        """get_dot("a.b.c")"""

        value = copy.deepcopy(self)
        to_pop = dot.split(".")

        while to_pop:
            next_key = to_pop.pop(0)
            value = value[next_key]

        return value


def substitute_brackets(dictionary, text) -> str:
    matches = BRACKET_PLACEHOLDER_RE.findall(text)

    if not matches:
        print("No brackets found.")
        return

    dot_dict = DotDict(dictionary)

    for m in matches:
        value = str(dot_dict.get_dot(m))
        text = text.replace(f"[[ {m} ]]", value)

    return text


def main(args) -> None:
    ssot_file = args[0]
    ssot_dictionary = None

    # Load dictionary from SSoT
    with open(ssot_file, "rb") as f:
        ssot_dictionary = tomllib.load(f)
        print(f"INFO: using dictionary {ssot_dictionary}")
        print()

    # Path of template(s) or enclosing folder
    target = Path(args[1]).resolve()
    if target.is_dir():
        templates = [f for f in target.iterdir() if TPL_FILE_RE.match(f.suffix)]
        if templates:
            print("FOUND:")
            for tpl in templates:
                print(tpl)
    elif target.is_file():
        with open(target, "r") as template:
            text = template.read()
            print(substitute_brackets(ssot_dictionary, text))
    else:
        print(f"Target '{target}' neither directory nor file.")
        sys.exit(1)


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print("USAGE: python3 ssot.toml target")
        sys.exit(1)

    main(args)
