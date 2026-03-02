from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from vibemouse.portable import setup_portable_env


class SetupPortableEnvTests(unittest.TestCase):
    def test_default_sets_modelscope_cache_to_portable_models_dir(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            setup_portable_env()
            cache = os.environ.get("MODELSCOPE_CACHE", "")

        from vibemouse.portable import get_models_dir
        self.assertEqual(cache, str(get_models_dir()))

    def test_vibemouse_models_dir_is_honoured_for_modelscope_cache(self) -> None:
        custom_dir = "/custom/models/path"
        with patch.dict(os.environ, {"VIBEMOUSE_MODELS_DIR": custom_dir}, clear=True):
            with patch("vibemouse.portable.Path.mkdir"):
                setup_portable_env()
            cache = os.environ.get("MODELSCOPE_CACHE", "")

        self.assertEqual(cache, custom_dir)

    def test_vibemouse_models_dir_is_honoured_for_hf_home(self) -> None:
        custom_dir = "/custom/models/path"
        with patch.dict(os.environ, {"VIBEMOUSE_MODELS_DIR": custom_dir}, clear=True):
            with patch("vibemouse.portable.Path.mkdir"):
                setup_portable_env()
            hf_home = os.environ.get("HF_HOME", "")

        self.assertEqual(hf_home, custom_dir + "/hf")

    def test_existing_modelscope_cache_is_not_overridden(self) -> None:
        preset = "/preset/cache"
        with patch.dict(os.environ, {"MODELSCOPE_CACHE": preset}, clear=True):
            with patch("vibemouse.portable.Path.mkdir"):
                setup_portable_env()
            cache = os.environ.get("MODELSCOPE_CACHE", "")

        self.assertEqual(cache, preset)
