#!/usr/bin/env python3

import tomllib

ssot = "ssot.toml"
target = "target.txt"

def main():
    with open(ssot, "rb") as f:
        data = tomllib.load(f)
        print(data)

if __name__ == "__main__":
    main()
