# Figma MCP Server

[![CI](https://github.com/creafly/figma-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/creafly/figma-mcp/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/creafly/figma-mcp)](https://github.com/creafly/figma-mcp/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/creafly/figma-mcp/pulls)

MCP server for working with Figma API.

## Features

- **get_file** - Get Figma file data
- **get_file_nodes** - Get specific nodes from a file
- **export_images** - Export node images
- **get_components** - Get file components
- **get_styles** - Get file styles
- **get_comments** - Get comments
- **get_team_projects** - Get team projects
- **get_project_files** - Get project files

## Installation

```bash
# Install dependencies
make install

# Or for development
make dev
```

## Configuration

Create a `.env` file:

```env
FIGMA_ACCESS_TOKEN=your_figma_personal_access_token
PORT=8002
HOST=0.0.0.0
LOG_LEVEL=INFO
```

## Running

```bash
make run
```

## Docker

```bash
docker build -t figma-mcp .
docker run -p 8002:8002 --env-file .env figma-mcp
```

## Tests

```bash
make test
```

## License

MIT
