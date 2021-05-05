@echo off
chcp 65001

echo --------------------------------------------------
echo 処理開始
echo.

cd src
call Scripts\activate.bat
python txt_to_md.py

echo.
echo 処理終了
pause