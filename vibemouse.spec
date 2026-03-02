# -*- mode: python ; coding: utf-8 -*-
"""
VibeMouse PyInstaller spec 文件
用法: pyinstaller vibemouse.spec
"""
from pathlib import Path

from PyInstaller.utils.hooks import collect_all  # noqa: F821 - available in spec context

project_dir = Path(SPECPATH)  # noqa: F821 - SPECPATH is injected by PyInstaller

# Collect all submodules + data for the large AI packages
_collect_pkgs = ["funasr", "funasr_onnx", "modelscope"]
_extra_datas: list = []
_extra_binaries: list = []
_extra_hidden: list = []
for _pkg in _collect_pkgs:
    try:
        _d, _b, _h = collect_all(_pkg, on_error="warn")
        _extra_datas += _d
        _extra_binaries += _b
        _extra_hidden += _h
    except Exception as _e:
        print(f"WARNING: could not collect '{_pkg}': {_e}")

a = Analysis(
    [str(project_dir / "vibemouse" / "main.py")],
    pathex=[str(project_dir)],
    binaries=_extra_binaries,
    datas=[
        (str(project_dir / "vibemouse"), "vibemouse"),
        *_extra_datas,
    ],
    hiddenimports=[
        "sounddevice",
        "soundfile",
        "pynput",
        "pynput.mouse",
        "pynput.keyboard",
        "comtypes",
        "onnxruntime",
        *_extra_hidden,
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
