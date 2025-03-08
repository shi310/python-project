import shutil
from pathlib import Path
from flutter.models.config import BuildConfig
from utils import consol

def run(path: Path, resource: Path):
    print()

    ios_path = path / "web"


    consol.log(f'正在更新 Web 文件 -> {ios_path}')
    
    resource_path = resource / "web"

    if resource_path.exists():
        shutil.copy(resource_path / "favicon.png", ios_path / "favicon.png")
        shutil.copy(resource_path / "icons/Icon-192.png", ios_path / "icons/Icon-192.png")
        shutil.copy(resource_path / "icons/Icon-512.png", ios_path / "icons/Icon-512.png")
        shutil.copy(resource_path / "icons/Icon-maskable-192.png", ios_path / "icons/Icon-maskable-192.png")
        shutil.copy(resource_path / "icons/Icon-maskable-512.png", ios_path / "icons/Icon-maskable-512.png")

        consol.succful("✅ IOS 资源文件已更新 ....")
