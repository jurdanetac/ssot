# frozen_string_literal: true

require_relative "ssot/version"

require "pathname"

require "toml"

module Ssot
  class Error < StandardError; end

  args = ARGF.argv

  if args.size != 2
    puts "USAGE: ruby lib/ssot.rb ssot.toml target"
    exit
  end

  ssot_file = Pathname args.first
  target = Pathname args.last
  ssot_hash = TOML::Parser.new(File.read(ssot_file)).parsed

  if target.file?
    puts "file"
  elsif target.directory?
    templates = target.glob("*.tpl")
    templates.each do |template|
      text = template.read
      # matches = text.scan(/(\[\[\s.*?\s\]\])/i)
      text.gsub!(/(\[\[\s(.*?)\s\]\])/i) do
        placeholder = ::Regexp.last_match(1)
        key = ::Regexp.last_match(2)

        sub_keys = key.split(".")
        value = ssot_hash.dig(*sub_keys)

        text = text.gsub(placeholder, value.to_s)
      end

      puts text
    end
  else
    puts "Target must be a file or a directory."
  end
end
