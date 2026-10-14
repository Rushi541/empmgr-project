# Employee Data Manager

## Purpose

Employee Data Manager is a Python-based command-line application for managing employee records. Employee information is stored in a JSON file and can be viewed or updated through an interactive menu.

Features include:

- List employees
- Add employees
- Email validation
- Salary validation
- Department summary reporting
- Rich-formatted table output

---

## Project Structure

```text
empmgr-project/
│
├── .gitignore
├── README.md
├── requirements.txt
│
├── data/
│   └── employees.json
│
└── empmgr/
    ├── __init__.py
    ├── models.py
    ├── storage.py
    ├── validators.py
    ├── report.py
    └── cli.py
```

---

## Setup

### Windows

Create a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the application:

```powershell
python -m empmgr.cli
```

---

### macOS / Linux

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m empmgr.cli
```

---

## Usage

Start the application:

```bash
python -m empmgr.cli
```

Menu:

```text
=== Employee Manager ===
1. List employees
2. Add employee
3. Quit
```

### Validation Rules

- Employee name cannot be empty.
- Email must be valid.
- Salary must be numeric.
- Salary cannot be negative.

---

## Notes

Run the application from the project root:

```bash
python -m empmgr.cli
```

Do not run:

```bash
python empmgr/cli.py
```

because relative imports may fail.

---

## Dependencies

This project uses:

- rich

Generate requirements file:

```bash
pip freeze > requirements.txt
```

---

## History

```text
*   ca33c50 Merge branch 'feature/report'
|\
| * cdc7559 add department summary
* | ddc554d Add email validation
|/
* 0a7ee2a Add main file
* ea415a0 Add module for validation
* c1f476a Add module for data storage
* 5ae87fd Add module for data model
* f652d97 Add init file for pakage
* 98681e3 Add emp data
* 553887f Add dependencies
* b0eb698 Add gitignore
```