from __future__ import annotations

"""Windows UIAutomation 焦点检测模块。

用法::

    from vibemouse.windows_focus import is_text_input_focused_win
    # 返回 True/False/None（None 表示检测失败，降级到剪切板）
"""


def is_text_input_focused_win() -> bool | None:
    """检测当前焦点是否在文本输入框（Edit 或 Document 控件）。

    优先尝试 comtypes + UIAutomation COM 接口；若不可用，返回 None。
    所有异常均被捕获，绝不抛出。
    """
    try:
        import comtypes.client  # type: ignore[import-untyped]

        comtypes.client.GetModule("UIAutomationCore.dll")
        import comtypes.gen.UIAutomationClient as uia  # type: ignore[import-untyped]

        automation = comtypes.client.CreateObject(
            "{ff48dba4-60ef-4201-aa87-54103eef594e}",
            interface=uia.IUIAutomation,
        )
        focused = automation.GetFocusedElement()
        if focused is None:
            return None
        control_type = focused.CurrentControlType
        # UIA_EditControlTypeId = 50004, UIA_DocumentControlTypeId = 50025
        return control_type in (50004, 50025)
    except Exception:
        return None
