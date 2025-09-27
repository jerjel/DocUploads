# build.py (alternative Python-based build)
import subprocess
import sys
from pathlib import Path

def build_package():
    """Build the package"""
    # Clean previous builds
    dist_dir = Path("dist")
    if dist_dir.exists():
        import shutil
        shutil.rmtree(dist_dir)
    
    build_dir = Path("build")
    if build_dir.exists():
        import shutil
        shutil.rmtree(build_dir)
    
    # Remove egg-info directories
    for egg_info in Path(".").glob("*.egg-info"):
        import shutil
        shutil.rmtree(egg_info)
    
    # Build the package
    subprocess.check_call([sys.executable, "-m", "build"])
    
    print("Build completed successfully!")
    print(f"Files created in {dist_dir}/:")
    for file in dist_dir.glob("*"):
        print(f"  {file}")

if __name__ == "__main__":
    build_package()

