# frozen_string_literal: true

require_relative "ssot/version"

require "pathname"

require "toml"

module Ssot
  class Error < StandardError; end

  class Parser
    attr_accessor :ssot

    def initialize(ssot_path)
      super()
      @ssot = TOML::Parser.new(File.read(ssot_path)).parsed
    end

    def process(target)
      # decide flow based on target path type
      if target.file?
        process_template target
      elsif target.directory?
        process_directory target
      else
        raise ArgumentError "Error"
      end
    end

    private

    def process_directory(directory)
      # get all templates in target directory
      templates = directory.glob("*.tpl")
      # iterate over each one and substitute the placeholders
      templates.each { |template| process_template template }
    end

    def process_template(template)
      text = template.read

      text.gsub!(/(\[\[\s(.*?)\s\]\])/i) do
        placeholder = ::Regexp.last_match(1)
        key = ::Regexp.last_match(2)

        sub_keys = key.split(".")
        value = ssot.dig(*sub_keys)

        text = text.gsub(placeholder, value.to_s)
      end

      puts text
    end
  end
end
