import re

from lib.util.FileUtil import FileUtil


def set_version() -> str:
    with open('pyproject.toml', 'r') as f:
        contents: str = f.read()
        version: str = re.search(r'^version = "([\d\.]+)"', contents, re.MULTILINE).group(1)
    FileUtil.str_to_file('lib/version.py', f'VERSION: str = "{version}"\n')
    return version


if __name__ == '__main__':
    set_version()
