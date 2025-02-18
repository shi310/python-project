import os
from pathlib import Path
import sys
import inquirer

project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from utils import cmd

# Flutter 版本路径
FLUTTER_VERSIONS = [
    "/opt/homebrew/Caskroom/flutter/3.24.3",
    "/opt/homebrew/Caskroom/flutter/3.27.2",
]

# .zshrc 文件路径
ZSHRC_FILE = os.path.expanduser("~/.zshrc")

# 函数：列出所有有效的 Flutter 版本
def list_versions():
    available_versions = []
    for version in FLUTTER_VERSIONS:
        expanded_version = os.path.expanduser(version)
        if os.path.exists(expanded_version):
            available_versions.append(expanded_version)
    return available_versions

# 函数：设置 Flutter 版本
def set_flutter_version(selected_version):
    # 检查路径是否存在
    if not os.path.exists(selected_version):
        print(f"Error: Flutter path '{selected_version}' does not exist.")
        return

    # 更新环境变量
    os.environ["PATH"] = f"{selected_version}/bin:{os.environ['PATH']}"
    print(f"Flutter version switched to: {selected_version}")

    # 更新 .zshrc 文件
    update_zshrc_with_flutter_path(selected_version)
    apply_current_version()  # 使当前脚本会话生效

# 函数：更新 .zshrc 文件中的 Flutter 路径
def update_zshrc_with_flutter_path(selected_version):
    if os.path.exists(ZSHRC_FILE):
        with open(ZSHRC_FILE, "r") as f:
            lines = f.readlines()

        # 移除旧的 Flutter 路径
        cleaned_lines = [
            line for line in lines 
            if not line.strip().startswith('export PATH="$PATH:/opt/homebrew/Caskroom/flutter/')
        ]

        # 添加新的 Flutter 路径
        # cleaned_lines.append(f'\n# Flutter environment\n')
        cleaned_lines.append(f'export PATH="$PATH:{selected_version}/bin"\n')

        # 写回文件
        with open(ZSHRC_FILE, "w") as f:
            f.writelines(cleaned_lines)

        print(f".zshrc updated with new Flutter path: {selected_version}/bin")
    else:
        # 如果 .zshrc 文件不存在，创建并添加
        with open(ZSHRC_FILE, "w") as f:
            f.write("# Flutter environment\n")
            f.write(f'export PATH="$PATH:{selected_version}/bin"\n')
        print(f".zshrc file created and Flutter path added: {selected_version}/bin")

# 函数：让当前脚本会话生效
def apply_current_version():
    print("Applying the Flutter version to the current session...")
    cmd.run("source ~/.zshrc", cwd='~/')

# 主逻辑
def main():
    # 获取有效的 Flutter 版本
    available_versions = list_versions()

    if not available_versions:
        print("No valid Flutter versions found in the system.")
        return

    # 用户选择 Flutter 版本
    questions = [
        inquirer.List(
            'flutter_version',
            message="Select Flutter version",
            choices=available_versions,
        ),
    ]
    answers = inquirer.prompt(questions)
    selected_version = answers['flutter_version']

    print(f"You selected: {selected_version}")
    set_flutter_version(selected_version)

if __name__ == "__main__":
    main()