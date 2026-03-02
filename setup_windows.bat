@echo off
setlocal

set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%.venv
set MODELS_DIR=%PROJECT_DIR%models

echo [1/5] 创建虚拟环境到项目目录...
python -m venv "%VENV_DIR%"
if errorlevel 1 (
    echo 错误：无法创建虚拟环境，请确认已安装 Python 3.10+
    pause
    exit /b 1
)

echo [2/5] 安装依赖...
"%VENV_DIR%\Scripts\pip.exe" install -U pip
"%VENV_DIR%\Scripts\pip.exe" install numpy "sounddevice>=0.4.6" "soundfile>=0.12.1" "pynput>=1.7.7" pyperclip "funasr>=1.2.6" "funasr-onnx>=0.4.1" "onnxruntime>=1.24.0" "modelscope>=1.18.0" comtypes pyinstaller

echo [3/5] 安装 VibeMouse 本身...
"%VENV_DIR%\Scripts\pip.exe" install -e "%PROJECT_DIR%"

echo [4/5] 下载 SenseVoice 模型到项目目录...
set MODELSCOPE_CACHE=%MODELS_DIR%
set HF_HOME=%MODELS_DIR%\hf
"%VENV_DIR%\Scripts\python.exe" -c "from modelscope.hub.snapshot_download import snapshot_download; snapshot_download('iic/SenseVoiceSmall'); snapshot_download('iic/SenseVoiceSmall-onnx')"

echo [5/5] 创建启动脚本...
(
echo @echo off
echo set PROJECT_DIR=%%~dp0
echo set MODELSCOPE_CACHE=%%PROJECT_DIR%%models
echo set HF_HOME=%%PROJECT_DIR%%models\hf
echo set VIBEMOUSE_BACKEND=funasr_onnx
echo set VIBEMOUSE_DEVICE=cpu
echo set VIBEMOUSE_AUTO_PASTE=true
echo set VIBEMOUSE_LANGUAGE=zh
echo "%%PROJECT_DIR%%.venv\Scripts\python.exe" -m vibemouse.main
) > "%PROJECT_DIR%run_windows.bat"

echo 完成！运行 run_windows.bat 启动 VibeMouse
pause
