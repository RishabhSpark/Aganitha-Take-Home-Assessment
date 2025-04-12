# Aganitha-Take-Home-Assessment

# get-papers-list

A Python CLI tool to fetch research papers from PubMed based on a user query, and identify papers with at least one author affiliated with a pharmaceutical or biotech company.

---

## Features

- Search PubMed using full query syntax
- Fetch metadata for research articles (title, authors, publication date, email, etc.)
- Identify non-academic authors and extract their company affiliations
- Output results to a clean CSV format
- Hybrid classification logic using heuristics + optional LLM fallback
- Built with modular, testable architecture and best practices
- Packaged with [Poetry](https://python-poetry.org/)

---

## Installation

Clone the repo and install dependencies via Poetry:

```bash
git clone https://github.com/RishabhSpark/Aganitha-Take-Home-Assessment.git
cd get-papers-list
poetry install
```

## Usage
Run the CLI from the root directory:

bash
```
poetry run get-papers-list --query "cancer immunotherapy" --file results.csv
```

CLI Options
Flag	Description
--query	PubMed search query (required)
--file	Output CSV file path
--debug	Enable debug logging
--help	Show help message