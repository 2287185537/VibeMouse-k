# -*- mode: python ; coding: utf-8 -*-
"""
VibeMouse PyInstaller spec 文件
用法: pyinstaller vibemouse.spec
"""
from __future__ import annotations

import sys
from pathlib import Path

project_dir = Path(SPECPATH)  # noqa: F821 – SPECPATH is injected by PyInstaller

a = Analysis(
    [str(project_dir / "vibemouse" / "main.py")],
    pathex=[str(project_dir)],
    binaries=[],
    datas=[
        (str(project_dir / "vibemouse"), "vibemouse"),
    ],
    hiddenimports=[
        "funasr",
        "funasr_onnx",
        "sounddevice",
        "soundfile",
        "pynput",
        "pynput.mouse",
        "pynput.keyboard",
        "comtypes",
        "modelscope",
        "onnxruntime",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "evdev",
        "gi",
        "gi.repository",
        "gi.repository.Atspi",
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)  # noqa: F821 – PYZ is injected by PyInstaller

exe = EXE(  # noqa: F821 – EXE is injected by PyInstaller
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="VibeMouse",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(  # noqa: F821 – COLLECT is injected by PyInstaller
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="VibeMouse",
)
