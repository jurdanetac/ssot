#!/usr/bin/env python3

import tomllib
import re

ssot = "ssot.toml"
target = "target.yaml"
bracket_regex = r"\[\[ (.*?) \]\]"

def main():
    ssot_values = None
    
    # Load dictionary from SSoT
    with open(ssot, "rb") as f:
        ssot_values = tomllib.load(f)

    # open target
    with open(target, "r+") as f:
        data = f.read()
    

        pattern = re.compile(bracket_regex)
        print(pattern.findall(data))
        
        
if __name__ == "__main__":
    main()
