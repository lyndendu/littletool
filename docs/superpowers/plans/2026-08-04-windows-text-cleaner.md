# Windows Text Cleaner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone Windows desktop text cleaner that normalizes full-width text, removes Unicode symbols and controls, converts tabs to spaces, and normalizes all carriage returns to line feeds.

**Architecture:** Keep transformation logic in a pure, independently testable module. Build a thin Tkinter desktop interface around it and use PyInstaller plus GitHub Actions for Windows packaging.

**Tech Stack:** Python 3.12, standard-library `tkinter` and `unicodedata`, `unittest`, PyInstaller, GitHub Actions Windows runner.

## Global Constraints

- Runtime must not require Python or extra software on the target Windows computer.
- `\r\n` and `\r` must become `\n`; existing `\n` stays unchanged.
- Tabs become one ASCII space.
- Full-width characters use Unicode NFKC conversion.
- Printable ASCII is preserved; non-ASCII Unicode symbols and control/format characters are deleted.
- Newline positions and counts are preserved after normalization.

---

### Task 1: Pure text transformation

**Files:**
- Create: `text-cleaner-windows/text_cleaner.py`
- Test: `text-cleaner-windows/tests/test_text_cleaner.py`

**Interfaces:**
- Produces: `clean_text(text: str) -> str`

- [ ] Write tests covering empty input, CRLF/CR normalization, tabs, full-width characters, punctuation, Chinese text, emoji/decorative symbols, and invisible controls.
- [ ] Run `python -m unittest discover -s text-cleaner-windows/tests -v` and confirm it fails because `text_cleaner` does not exist.
- [ ] Implement `clean_text` using newline replacement, tab replacement, NFKC normalization, and Unicode-category filtering.
- [ ] Run the complete test suite and confirm all tests pass.

### Task 2: Tkinter desktop interface

**Files:**
- Create: `text-cleaner-windows/app.py`

**Interfaces:**
- Consumes: `clean_text(text: str) -> str`
- Produces: executable GUI entry point `main() -> None`

- [ ] Build input and output text areas with scrollbars.
- [ ] Add Convert, Copy Result, and Clear actions.
- [ ] Display action results and clipboard failures in a status label.
- [ ] Validate module syntax with `python -m py_compile text-cleaner-windows/app.py text-cleaner-windows/text_cleaner.py`.

### Task 3: Windows packaging and documentation

**Files:**
- Create: `text-cleaner-windows/build_windows.bat`
- Create: `text-cleaner-windows/requirements-build.txt`
- Create: `text-cleaner-windows/README.md`
- Create: `.github/workflows/build-text-cleaner-windows.yml`

**Interfaces:**
- Produces: `dist/TextCleaner.exe` locally and a `TextCleaner-Windows` workflow artifact.

- [ ] Add a repeatable PyInstaller batch script using `--onefile --windowed`.
- [ ] Add a Windows GitHub Actions job that runs tests, builds the executable, smoke-checks the artifact path, and uploads it.
- [ ] Document end-user use, local source execution, local Windows builds, transformation rules, and workflow artifact download steps.
- [ ] Run final unit tests and syntax checks.
