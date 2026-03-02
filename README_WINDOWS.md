# VibeMouse Windows 使用指南

## 系统要求

- Windows 10 64 位或更新版本
- Python 3.10 或更新版本（[下载地址](https://www.python.org/downloads/)）
- 麦克风（需在系统设置中授予麦克风权限）
- 带侧键的鼠标（通常为 X1/X2 按键）

## 快速开始

### 第一步：初始化环境

双击运行 `setup_windows.bat`，脚本将自动完成：

1. 在项目目录下创建 Python 虚拟环境（`.venv\`）
2. 安装所有依赖包
3. 下载 SenseVoice 语音识别模型到 `models\` 目录
4. 生成启动脚本 `run_windows.bat`

> **注意**：首次运行需要下载约 400 MB 的 AI 模型，请确保网络畅通。
> 所有文件均保存在项目目录内，不会向 C 盘用户目录写入任何内容。

### 第二步：启动 VibeMouse

双击运行 `run_windows.bat`。

启动后：
- 按鼠标**前侧键**（X1）开始录音，再次按下停止并转写
- 按鼠标**后侧键**（X2）执行其他操作（录音中：停止并发送到 OpenClaw；空闲时：发送回车）
- 转写结果自动粘贴到当前焦点位置

## 环境变量配置

可在 `run_windows.bat` 中修改以下环境变量：

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `VIBEMOUSE_BACKEND` | `funasr_onnx` | 转写后端（`funasr_onnx` / `funasr` / `auto`） |
| `VIBEMOUSE_DEVICE` | `cpu` | 推理设备（`cpu` / `cuda`） |
| `VIBEMOUSE_LANGUAGE` | `zh` | 识别语言（`zh` / `en` / `auto`） |
| `VIBEMOUSE_AUTO_PASTE` | `true` | 是否自动粘贴 |
| `VIBEMOUSE_MODELS_DIR` | `项目目录\models` | 模型缓存目录 |

## 常见问题

### 侧键不响应

- 确认鼠标已连接，侧键在其他软件中可正常使用
- 以管理员权限运行 `run_windows.bat`
- 检查是否有其他软件独占了鼠标输入（如鼠标驱动软件）

### 首次启动很慢

首次启动需要加载 AI 模型（约数秒到数十秒），属于正常现象。
后续启动速度将明显加快。

### 模型下载失败

- 检查网络连接，必要时配置代理
- 手动下载模型并放置到 `models\` 目录：
  ```
  set MODELSCOPE_CACHE=<项目目录>\models
  python -c "from modelscope.hub.snapshot_download import snapshot_download; snapshot_download('iic/SenseVoiceSmall'); snapshot_download('iic/SenseVoiceSmall-onnx')"
  ```

### 识别结果不准确

- 确保麦克风音量适中，背景噪音较小
- 尝试将 `VIBEMOUSE_LANGUAGE` 设置为具体语言（如 `zh` 或 `en`）而非 `auto`

### 提示"找不到虚拟环境"

请先运行 `setup_windows.bat` 完成初始化。

## 打包为可执行文件

如需将 VibeMouse 打包为无需 Python 环境的独立程序，运行 `build_windows.bat`。

打包完成后，可执行文件位于 `dist\VibeMouse\` 目录。

> **注意**：打包后的程序不包含 AI 模型，首次运行仍需下载模型。
> 将 `models\` 目录复制到 `dist\VibeMouse\` 旁边即可离线使用。

## 项目目录结构

```
VibeMouse-k\
├── .venv\              # Python 虚拟环境（由 setup_windows.bat 创建）
├── models\             # AI 模型缓存（由 setup_windows.bat 下载）
├── vibemouse\          # 源代码
├── setup_windows.bat   # 初始化脚本
├── run_windows.bat     # 启动脚本（由 setup_windows.bat 生成）
├── build_windows.bat   # 打包脚本
└── vibemouse.spec      # PyInstaller 配置
```
