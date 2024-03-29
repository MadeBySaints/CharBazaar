@echo off
echo Running kills.py...
python kills.py
timeout /t 1 /nobreak >nul

echo Running list.py...
python list.py
timeout /t 1 /nobreak >nul

echo Running merge.py...
python merge.py
timeout /t 1 /nobreak >nul

echo All scripts executed successfully.
pause
