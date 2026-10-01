# odd-quest

一把离线故事骰子：随机组合地点、麻烦和反转，快速得到一个中文故事灵感。适合写作热身、桌游跑团和脑暴。

## 使用

需要 Python 3.8+，无需安装依赖，也不会联网。

```sh
python odd_quest.py
```

Windows 上也可以运行：

```powershell
py .\odd_quest.py
```

输出会附上数字种子；在相同 Python 版本下用它复现：

```sh
python odd_quest.py --seed 17
```

## 许可

MIT，见 [LICENSE](LICENSE)。
## Linux x86_64 下载

- [单文件版](https://github.com/506058115-cmd/odd-quest/releases/download/v1.0.0/odd-quest-linux-x86_64-onefile.tar.gz)
- [目录版](https://github.com/506058115-cmd/odd-quest/releases/download/v1.0.0/odd-quest-linux-x86_64-onedir.tar.gz)
- [v1.0.0 Release 页面](https://github.com/506058115-cmd/odd-quest/releases/tag/v1.0.0)

压缩包附带构建信息和依赖许可证；Release 另附 SHA-256 校验文件。产物在 WSL Ubuntu 24.04（Python 3.12.3、PyInstaller 6.22.2）中构建，目标为 GNU/Linux x86_64。较旧的发行版可能需要兼容的 glibc。
