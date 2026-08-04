@echo off
setlocal

cd /d "%~dp0"

python -m pip install --upgrade pip
if errorlevel 1 exit /b 1

python -m pip install -r requirements-build.txt
if errorlevel 1 exit /b 1

python -m unittest discover -s tests -v
if errorlevel 1 exit /b 1

python -m PyInstaller ^
  --noconfirm ^
  --clean ^
  --onefile ^
  --windowed ^
  --name TextCleaner ^
  app.py
if errorlevel 1 exit /b 1

if not exist "dist\TextCleaner.exe" (
  echo Build failed: dist\TextCleaner.exe was not created.
  exit /b 1
)

echo.
echo Build complete: %CD%\dist\TextCleaner.exe
endlocal
