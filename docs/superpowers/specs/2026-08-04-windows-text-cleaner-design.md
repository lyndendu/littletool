# Windows Text Cleaner Design

## Goal

Create a small local desktop utility written in Python that can be distributed as a standalone Windows executable. Users paste text, convert it, and copy the cleaned result without installing Python or any other runtime.

## Text transformation rules

1. Convert Windows newlines (`\r\n`) and standalone carriage returns (`\r`) to line feeds (`\n`).
2. Replace every tab (`\t`) with one ordinary ASCII space.
3. Apply Unicode NFKC normalization so full-width Latin letters, digits, punctuation, and ideographic spaces become their half-width equivalents where Unicode defines one.
4. Preserve line feeds, ordinary spaces, letters, numbers, combining marks, and Unicode punctuation.
5. Preserve printable ASCII after normalization, but delete control/format characters and non-ASCII Unicode symbol-category characters, including emoji, decorative symbols, currency symbols, and mathematical symbols.
6. Preserve the number and position of line feeds after newline normalization.

## Architecture

- `text_cleaner.py` contains a pure `clean_text(text: str) -> str` function with no GUI dependencies.
- `app.py` contains a Tkinter GUI with input/output text areas and Convert, Copy Result, and Clear buttons.
- `tests/test_text_cleaner.py` covers newline normalization, tabs, full-width conversion, punctuation preservation, multilingual text, symbols, and invisible controls.
- `build_windows.bat` packages the application with PyInstaller.
- GitHub Actions builds and uploads a standalone Windows `.exe` artifact.

## Error handling

The converter accepts an empty string and returns an empty string. GUI clipboard errors are displayed in the status label rather than crashing the program.

## Distribution

The runtime uses only Python's standard library. PyInstaller is a build-time dependency only. The resulting `TextCleaner.exe` runs on Windows without Python installed.
