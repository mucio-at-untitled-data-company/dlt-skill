# data-skills

A collection of Claude Code skills for data engineering tasks.

## Overview

This repository contains expert assistant skills designed to help with data engineering workflows. Each skill provides specialized knowledge, templates, and best practices for specific data tools and patterns.

## Available Skills

| Skill | Description | Version |
|-------|-------------|---------|
| [dlt-skill](skills/dlt-skill/) | Expert guidance for building data pipelines with [dlt](https://dlthub.com) (data load tool) | 0.1.0 |

## Installation

Install skills using the Claude Code CLI:

```bash
npx @anthropic-ai/claude-code skills add untitled-data-company/data-skills --skill <skill-name>
```

For example, to install the dlt-skill:

```bash
npx @anthropic-ai/claude-code skills add untitled-data-company/data-skills --skill dlt-skill
```

### Verify Installation

After installation, the skill should appear when you run `/skills` in Claude Code.

## Repository Structure

```
data-skills/
├── skills/
│   └── dlt-skill/       # dlt pipeline skill
│       ├── SKILL.md     # Main skill instructions
│       ├── README.md    # Skill documentation
│       ├── assets/      # Templates and configurations
│       ├── references/  # Reference documentation
│       └── scripts/     # Helper scripts
├── README.md            # This file
└── CHANGELOG.md         # Version history
```

## Contributing

To add a new skill:
1. Create a new directory under `skills/`
2. Add a `SKILL.md` with the skill instructions
3. Add a `README.md` with documentation
4. Include any templates, references, or scripts needed

## License

Skills in this repository are provided as-is for use with Claude and other skill-enabled LLMs. Maintained by [Untitled Data Company](https://untitleddata.company/).
