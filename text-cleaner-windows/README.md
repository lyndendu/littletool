# Windows 文本清理工具

一个使用 Python 和 Tkinter 编写的本地桌面工具。打包后的 `TextCleaner.exe` 可以直接在 Windows 电脑运行，不需要安装 Python 或其他运行环境。

## 功能

- 将 `\r\n` 和单独的 `\r` 统一转换为 `\n`。
- 原有 `\n` 保持不变，包括连续换行和结尾换行。
- 每个制表符 `Tab` 转换为一个普通空格。
- 将全角英文字母、数字、空格和标点转换为半角形式。
- 将 `。、【】《》“”‘’—` 等常见中文标点转换为对应 ASCII 标点。
- 保留中文、其他语言文字、数字、普通标点和可打印 ASCII 字符。
- 删除 Emoji、装饰符号、非 ASCII 货币/数学符号、零宽字符和其他不可见控制字符。

## Windows 用户直接使用

1. 打开仓库的 **Actions** 页面。
2. 选择 **Build Text Cleaner for Windows**。
3. 打开最近一次成功的构建记录。
4. 在 **Artifacts** 区域下载 `TextCleaner-Windows`。
5. 解压后双击 `TextCleaner.exe`。

> `.exe` 由 Windows GitHub Actions 运行器生成，不直接提交到 Git 仓库中。

程序提供：

- 原始文本输入框
- 处理结果输出框
- `转换文本` 按钮
- `复制结果` 按钮
- `清空` 按钮

也可以按 `Ctrl + Enter` 执行转换。

## 使用源码运行

已安装 Python 3.10 或更高版本时：

```bash
cd text-cleaner-windows
python app.py
```

运行转换规则测试：

```bash
python -m unittest discover -s tests -v
```

运行程序不需要第三方 Python 包。

## 在 Windows 本地生成 EXE

已安装 Python 的开发电脑可以双击：

```text
build_windows.bat
```

或在命令提示符中运行：

```bat
cd text-cleaner-windows
build_windows.bat
```

生成结果：

```text
text-cleaner-windows\dist\TextCleaner.exe
```

PyInstaller 只用于构建。最终用户运行 `.exe` 时不需要安装 PyInstaller 或 Python。

## 转换示例

输入：

```text
ＡＢＣ　１２３，。！？
第一行\r\n第二行\t😀★
```

处理后的实际换行内容等效于：

```text
ABC 123,.!?
第一行
第二行 
```
