# Employee Data Manager

A simple employee management application built as a Python package.

## Setup

### Windows

Create virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run application:

```powershell
python -m empmgr.cli
```

---

### macOS/Linux

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python -m empmgr.cli
```

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