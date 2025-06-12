# cloudvenv_cli.py (polished version)
import os
import sys
import json
import shutil
import tarfile
import urllib.request
from pathlib import Path

REPO_BASE_URL = "https://raw.githubusercontent.com/deepmarathe/cloudvenv/main"
DEFAULT_ENV = "top-packages-env"
VENV_DIR = Path.home() / ".cloudvenv"
VENV_METADATA = f"{REPO_BASE_URL}/venvs/metadata.json"


def fetch_metadata():
    try:
        with urllib.request.urlopen(VENV_METADATA) as response:
            return json.load(response)
    except Exception as e:
        print(f"Failed to fetch metadata: {e}")
        return {}


def list_envs():
    metadata = fetch_metadata()
    print("Available Environments:")
    for name, info in metadata.items():
        print(f"  - {name}: {info.get('description', '')}")


def download_and_extract(env_name):
    tar_url = f"{REPO_BASE_URL}/venvs/{env_name}.tar.gz"
    dest_dir = VENV_DIR / env_name
    tar_path = VENV_DIR / f"{env_name}.tar.gz"

    print(f"⬇️  Downloading {env_name}...")
    VENV_DIR.mkdir(exist_ok=True)
    urllib.request.urlretrieve(tar_url, tar_path)

    print("📂 Extracting...")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=VENV_DIR)
    tar_path.unlink()
    print(f"✅ Extracted to {dest_dir}")


def activate_hint(env_name):
    env_path = VENV_DIR / env_name / "bin" / "activate"
    if env_path.exists():
        print(f"🔗 To activate, run:")
        print(f"    source {env_path}")
    else:
        print(f"❌ Activation script not found in {env_path}")


def install(env_name):
    download_and_extract(env_name)
    activate_hint(env_name)


def run_help():
    print("""
CloudVenv CLI
Usage:
  python cloudvenv_cli.py list
  python cloudvenv_cli.py install [env-name]
  (or run without arguments to install the default environment)
    """)


def main():
    if len(sys.argv) < 2:
        install(DEFAULT_ENV)
        return

    command = sys.argv[1]
    if command == "list":
        list_envs()
    elif command == "install":
        env = sys.argv[2] if len(sys.argv) == 3 else DEFAULT_ENV
        install(env)
    else:
        run_help()


if __name__ == "__main__":
    main()
