# PediPy

**PediPy** is an educational Python-based pedigree analysis tool designed to represent family relationships and explore genetic pedigrees.

This project is being developed as a hands-on learning exercise in Python, object-oriented programming, software design, and automated testing.

## Current Features

- Represent individuals using a `Person` class.
- Store individuals in a `Pedigree` structure.
- Identify parent-child relationships.
- Identify full and half siblings.
- Identify grandparent-grandchild relationships.
- Validate pedigree data, including missing parent references and parent-sex conflicts.
- Prevent duplicate individual IDs.

## Project Structure

```text
PediPy/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── person.py
│   └── pedigree.py
├── data/
├── tests/
│   └── test_pedigree.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.13 or compatible Python 3 version
- Dependencies listed in 'requirments.txt'
Install dependencies:

```bash
pip install -r requirements.txt
## Running Tests

Clone the repository and navigate into the project directory.

Run:

```bash
python -m pytest -v
```

## Development Status

**Work in Progress — Version 1.0 is under development.**

Planned development includes:
- Additional family relationship analysis.
- JSON-based pedigree data loading.
- Basic pedigree visualization.
- An educational genetic inheritance analysis feature.
- Documentation and code-quality improvements.

## Project Scope

PediPy is an educational project. It is not intended for clinical diagnosis or medical decision-making.
