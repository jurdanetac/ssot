# frozen_string_literal: true

require_relative "ssot/version"
require "toml"

module Ssot
  class Error < StandardError; end

  args = ARGF.argv

  if args.size != 2
    puts "USAGE: ruby lib/ssot.rb ssot.toml target"
    exit
  end

  ssot_file, target_path = args
  ssot_hash = TOML::Parser.new(File.read(ssot_file)).parsed
end

=begin
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
=end
