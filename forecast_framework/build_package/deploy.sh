#!/bin/bash
# deploy.sh

set -e  # Exit on any error

echo "Starting deployment to Artifactory..."

# Validate required environment variables
if [ -z "$ARTIFACTORY_URL" ] || [ -z "$ARTIFACTORY_USERNAME" ] || [ -z "$ARTIFACTORY_API_KEY" ]; then
    echo "Error: Missing required environment variables"
    echo "Please set: ARTIFACTORY_URL, ARTIFACTORY_USERNAME, ARTIFACTORY_API_KEY"
    exit 1
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Build the package
echo "Building package..."
python -m build

if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi

# Set twine configuration
export TWINE_USERNAME="$ARTIFACTORY_USERNAME"
export TWINE_PASSWORD="$ARTIFACTORY_API_KEY"
export TWINE_REPOSITORY_URL="$ARTIFACTORY_URL"

# Upload to Artifactory
echo "Uploading to Artifactory..."
python -m twine upload --repository-url "$ARTIFACTORY_URL" dist/*

if [ $? -eq 0 ]; then
    echo "Deployment successful!"
    echo "Package uploaded to: $ARTIFACTORY_URL"
else
    echo "Deployment failed!"
    exit 1
fi