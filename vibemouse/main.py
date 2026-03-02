from __future__ import annotations

from vibemouse.portable import setup_portable_env

setup_portable_env()  # 必须在所有其他 import 之前调用

from vibemouse.app import VoiceMouseApp
from vibemouse.config import load_config


def main() -> None:
    config = load_config()
    app = VoiceMouseApp(config)
    app.run()


if __name__ == "__main__":
    main()
