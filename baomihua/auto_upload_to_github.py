#!/usr/bin/env python3
"""
自动上传项目到 GitHub 仓库
"""
import subprocess
import os
from pathlib import Path

def run_command(cmd, cwd=None):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def main():
    repo_dir = r'C:\Users\ASUS\Downloads\baomihua\baomihua'
    github_url = 'https://github.com/Crimsonzsy66/zsy112304260145.git'
    branch = 'main'

    print("=" * 60)
    print("  自动上传到 GitHub")
    print("=" * 60)
    print()

    # 1. 检查git
    print("1. 检查 Git 安装...")
    code, stdout, stderr = run_command('git --version', repo_dir)
    if code == 0:
        print(f"   ✓ {stdout.strip()}")
    else:
        print("   ✗ Git 未安装")
        print("   请先安装 Git: https://git-scm.com/download/win")
        return False

    # 2. 检查目录
    print()
    print(f"2. 进入目录: {repo_dir}")
    if not os.path.exists(repo_dir):
        print("   ✗ 目录不存在")
        return False
    print("   ✓ 目录存在")

    # 3. 初始化git
    print()
    print("3. 初始化 Git 仓库...")
    if not os.path.exists(os.path.join(repo_dir, '.git')):
        code, stdout, stderr = run_command('git init', repo_dir)
        if code == 0:
            print("   ✓ Git 仓库已初始化")
        else:
            print(f"   ✗ 初始化失败: {stderr}")
            return False
    else:
        print("   ✓ Git 仓库已存在")

    # 4. 配置远程仓库
    print()
    print("4. 配置远程仓库...")
    code, stdout, stderr = run_command('git remote -v', repo_dir)
    if 'origin' in stdout:
        code, stdout, stderr = run_command('git remote set-url origin ' + github_url, repo_dir)
        print("   ✓ 远程仓库已更新")
    else:
        code, stdout, stderr = run_command('git remote add origin ' + github_url, repo_dir)
        if code == 0:
            print("   ✓ 远程仓库已添加")
        else:
            print(f"   ✗ 添加远程仓库失败: {stderr}")
            return False

    # 5. 配置用户信息（如果需要）
    print()
    print("5. 配置 Git 用户信息...")
    code, _, _ = run_command('git config user.name', repo_dir)
    if code != 0:
        run_command('git config user.name "Crimsonzsy66"', repo_dir)
        run_command('git config user.email "user@github.com"', repo_dir)
        print("   ✓ 用户信息已配置")

    # 6. 添加文件
    print()
    print("6. 添加文件到暂存区...")
    code, stdout, stderr = run_command('git add -A', repo_dir)
    if code == 0:
        print("   ✓ 文件已添加")
    else:
        print(f"   ✗ 添加文件失败: {stderr}")
        return False

    # 7. 检查状态
    print()
    print("7. 检查提交状态...")
    code, stdout, stderr = run_command('git status', repo_dir)
    if 'nothing to commit' in stdout:
        print("   ⚠ 没有新文件需要提交")
        print("   跳过提交步骤")
    else:
        # 8. 提交
        print()
        print("8. 提交更改...")
        commit_msg = "更新代码和实验报告 - 周思言 112304260145"
        code, stdout, stderr = run_command(f'git commit -m "{commit_msg}"', repo_dir)
        if code == 0:
            print(f"   ✓ 已提交: {commit_msg}")
        else:
            print(f"   ⚠ 提交失败或没有更改需要提交")

    # 9. 推送到GitHub
    print()
    print("9. 推送到 GitHub...")
    print("   提示: 如果是首次推送，可能需要输入 GitHub 用户名和密码")
    print("   用户名: Crimsonzsy66")
    print("   密码/Token: [请输入你的 GitHub Password 或 Personal Access Token]")
    print()

    # 使用 credential helper
    run_command('git config credential.helper store', repo_dir)

    code, stdout, stderr = run_command(
        f'git push -u origin {branch} --force',
        repo_dir
    )

    if code == 0:
        print()
        print("=" * 60)
        print("  ✓ 推送成功！")
        print("=" * 60)
        print()
        print("仓库地址: https://github.com/Crimsonzsy66/zsy112304260145")
        print()
        return True
    else:
        print()
        print("=" * 60)
        print("  ⚠ 推送失败")
        print("=" * 60)
        print()
        print("可能的原因:")
        print("1. 需要手动输入用户名和密码")
        print("2. 网络连接问题")
        print("3. 仓库不存在或权限不足")
        print()
        print("建议操作:")
        print("1. 打开 Git Bash")
        print("2. 运行: cd C:\\Users\\ASUS\\Downloads\\baomihua\\baomihua")
        print("3. 运行: git push -u origin main")
        print("4. 按提示输入用户名和密码/Token")
        print()
        return False

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n错误: {e}")
    input("\n按 Enter 键退出...")
