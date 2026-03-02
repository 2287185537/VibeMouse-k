from __future__ import annotations

"""
便携模式：所有运行时文件（模型缓存、临时音频、状态文件）
都存放在项目根目录下，不写入系统目录。
"""

from pathlib import Path


def get_project_root() -> Path:
    """返回项目根目录（vibemouse 包的上级目录）"""
    import sys

    if getattr(sys, "frozen", False):
        # PyInstaller 打包后，exe 所在目录为项目根
        return Path(sys.executable).parent
    return Path(__file__).parent.parent


def get_models_dir() -> Path:
    return get_project_root() / "models"


def get_temp_dir() -> Path:
    return get_project_root() / "temp"


def get_status_file() -> Path:
    return get_project_root() / "vibemouse-status.json"


def setup_portable_env() -> None:
    """在进程启动时设置所有缓存环境变量，确保不写入系统目录"""
    import os

    # If the user explicitly set VIBEMOUSE_MODELS_DIR, honour it as the cache
    # root so that config.py's later setdefault calls are consistent.
    # Otherwise fall back to the portable default next to the exe/project.
    custom_models_dir = os.getenv("VIBEMOUSE_MODELS_DIR")
    if custom_models_dir:
        models_dir = Path(custom_models_dir)
    else:
        models_dir = get_models_dir()
    models_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("MODELSCOPE_CACHE", str(models_dir))
    os.environ.setdefault("HF_HOME", str(models_dir / "hf"))
    os.environ.setdefault("TORCH_HOME", str(models_dir / "torch"))
    os.environ.setdefault("VIBEMOUSE_TEMP_DIR", str(get_temp_dir()))
    os.environ.setdefault("VIBEMOUSE_STATUS_FILE", str(get_status_file()))
