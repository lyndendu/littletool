"""Tkinter desktop interface for the Windows text cleaner."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from text_cleaner import clean_text


class TextCleanerApp(ttk.Frame):
    """Small desktop interface for pasting, cleaning, and copying text."""

    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master, padding=16)
        self.master = master
        self.status = tk.StringVar(value="请粘贴需要处理的文本。")
        self._build_ui()

    def _build_ui(self) -> None:
        self.grid(row=0, column=0, sticky="nsew")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(4, weight=1)

        ttk.Label(self, text="原始文本", font=("Microsoft YaHei UI", 11, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 6)
        )
        self.input_text = self._create_text_area(row=1)

        button_bar = ttk.Frame(self)
        button_bar.grid(row=2, column=0, sticky="ew", pady=12)
        ttk.Button(button_bar, text="转换文本", command=self.convert).pack(side="left")
        ttk.Button(button_bar, text="复制结果", command=self.copy_result).pack(side="left", padx=8)
        ttk.Button(button_bar, text="清空", command=self.clear).pack(side="left")

        ttk.Label(self, text="处理结果", font=("Microsoft YaHei UI", 11, "bold")).grid(
            row=3, column=0, sticky="w", pady=(0, 6)
        )
        self.output_text = self._create_text_area(row=4)

        ttk.Label(self, textvariable=self.status, anchor="w").grid(
            row=5, column=0, sticky="ew", pady=(10, 0)
        )

        self.master.bind("<Control-Return>", lambda _event: self.convert())
        self.input_text.focus_set()

    def _create_text_area(self, row: int) -> tk.Text:
        container = ttk.Frame(self)
        container.grid(row=row, column=0, sticky="nsew")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        text_widget = tk.Text(
            container,
            wrap="word",
            undo=True,
            font=("Microsoft YaHei UI", 10),
            padx=10,
            pady=10,
        )
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar.set)
        text_widget.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        return text_widget

    def convert(self) -> None:
        source = self.input_text.get("1.0", "end-1c")
        result = clean_text(source)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)
        self.status.set(f"转换完成：输入 {len(source)} 个字符，输出 {len(result)} 个字符。")

    def copy_result(self) -> None:
        result = self.output_text.get("1.0", "end-1c")
        try:
            self.master.clipboard_clear()
            self.master.clipboard_append(result)
            self.master.update_idletasks()
        except tk.TclError as error:
            self.status.set(f"复制失败：{error}")
            return
        self.status.set("结果已复制到剪贴板。")

    def clear(self) -> None:
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.status.set("内容已清空。")
        self.input_text.focus_set()


def main() -> None:
    root = tk.Tk()
    root.title("文本清理工具")
    root.geometry("900x680")
    root.minsize(640, 480)
    TextCleanerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
