# SSoT (Single Source of Truth)

> A lightweight Ruby gem and CLI tool that compiles `.jtpl` templates into synchronized configuration files using a single TOML dataset.

## Why SSoT?
Managing shared configuration parameters across multiple formats (`YAML`, `TOML`, `Terraform/HCL`) often leads to drift and duplicate definitions. **SSoT** allows you to maintain one centralized TOML definition and compile your application and infrastructure configs seamlessly.

### Features
- **Zero Configuration Drift:** Update values once in `ssot.toml`, compile everywhere.
- **Deep Path Lookup:** Use dot notation (`[[ db.primary.host ]]`) to resolve nested TOML structures.
- **Batch Processing:** Target individual files or recursively process entire directory trees.
- **Auto Headers:** Automatically timestamps and tags generated configuration files.

## Usage

`USAGE: ssot ssot.toml target`

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jurdanetac/ssot.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
