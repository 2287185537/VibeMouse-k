@echo off
setlocal
set PROJECT_DIR=%~dp0
set VENV_PYTHON=%PROJECT_DIR%.venv\Scripts\python.exe

if not exist "%VENV_PYTHON%" (
    echo 错误：找不到虚拟环境，请先运行 setup_windows.bat
    pause
    exit /b 1
)

echo [打包] 使用 PyInstaller 打包 VibeMouse...

"%VENV_PYTHON%" -m PyInstaller ^
  --name VibeMouse ^
  --onedir ^
  --windowed ^
  --add-data "%PROJECT_DIR%vibemouse;vibemouse" ^
  --hidden-import funasr ^
  --hidden-import funasr_onnx ^
  --hidden-import sounddevice ^
  --hidden-import soundfile ^
  --hidden-import pynput ^
  --hidden-import pynput.mouse ^
  --hidden-import pynput.keyboard ^
  --hidden-import comtypes ^
  --hidden-import modelscope ^
  --hidden-import onnxruntime ^
  --collect-all funasr ^
  --collect-all funasr_onnx ^
  --collect-all modelscope ^
  --exclude-module evdev ^
  --exclude-module gi ^
  --noconfirm ^
  "%PROJECT_DIR%vibemouse\main.py"

echo [完成] 输出在 dist\VibeMouse\ 目录
pause
