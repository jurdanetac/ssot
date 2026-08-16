# SSoT (Single Source of Truth)

> A lightweight Ruby gem and CLI tool that compiles `.jtpl` templates into synchronized configuration files using a single TOML dataset.

## Why SSoT?
Managing shared configuration parameters across multiple formats (`YAML`, `TOML`, `Terraform/HCL`) often leads to drift and duplicate definitions. **SSoT** allows you to maintain one centralized TOML definition and compile your application and infrastructure configs seamlessly.

### Features
- **Zero Configuration Drift:** Update values once in `ssot.toml`, compile everywhere.
- **Deep Path Lookup:** Use dot notation (`[[ db.primary.host ]]`) to resolve nested TOML structures.
- **Batch Processing:** Target individual files or recursively process entire directory trees.
- **Auto Headers:** Automatically timestamps and tags generated configuration files.

## Installation

TODO: Write installation instructions here

## Usage

TODO: Write usage instructions here

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake test` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and the created tag, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jurdanetac/ssot.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
