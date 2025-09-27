# build.sh
#!/bin/bash
set -e

echo "Building forecasting-framework..."

# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build wheel and source distribution
python -m build

echo "Build completed successfully!"
echo "Files created:"
ls -la dist/