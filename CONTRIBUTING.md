# Contributing to data-skills

Thank you for your interest in contributing to data-skills!

## Adding a New Skill

1. **Create the skill directory**
   ```
   skills/<skill-name>/
   ├── SKILL.md          # Required: Main instructions with YAML frontmatter
   ├── references/       # Optional: Reference documentation
   ├── assets/           # Optional: Templates, configs, static files
   └── scripts/          # Optional: Helper scripts
   ```

2. **Write SKILL.md with proper frontmatter**
   ```yaml
   ---
   name: skill-name
   description: >
     Brief description of what the skill does and when to use it.
     Include trigger phrases and use cases.
   ---
   ```

3. **Add user documentation**
   - Create `docs/<skill-name>.md` with user-facing guide
   - Include installation, features, and usage examples

4. **Update the README**
   - Add an entry to the "Available Skills" table in the root README.md

## Skill Structure Guidelines

- **SKILL.md**: Keep under 500 lines. Move detailed content to `references/`
- **references/**: Documentation Claude reads as needed (schemas, API docs, guides)
- **assets/**: Files used in output (templates, configs) - not loaded into context
- **scripts/**: Executable helpers (Python/Bash) with proper shebangs

## Code Standards

- Python scripts should have `#!/usr/bin/env python3` shebang
- Scripts should be executable (`chmod +x`)
- Include docstrings for complex functions
- Test scripts before committing

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-skill`)
3. Make your changes following the guidelines above
4. Update CHANGELOG.md under `[Unreleased]`
5. Submit a pull request with a clear description

## Questions?

Open an issue or reach out to [Untitled Data Company](https://untitleddata.company/).
