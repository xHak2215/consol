pip install pyinstaller
pyinstaller --version
@echo off
echo input name py file 
set /p input= file 
echo file %input%
pyinstaller --onefile %input%
pass
pausse