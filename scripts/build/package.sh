#!/bin/bash
# Package script for Transcendent application

set -e

echo "Packaging Transcendent application..."

VERSION=${1:-"1.0.0"}
PACKAGE_DIR="package/transcendent-${VERSION}"

# Create package directory
mkdir -p "${PACKAGE_DIR}/bin"
mkdir -p "${PACKAGE_DIR}/lib"
mkdir -p "${PACKAGE_DIR}/config"

# Build the application first
./scripts/build/build.sh

# Copy binary
cp bazel-bin/src/main/cpp/transcendent "${PACKAGE_DIR}/bin/"

# Copy configuration files
cp -r config/environments/production/* "${PACKAGE_DIR}/config/"

# Create archive
tar -czf "transcendent-${VERSION}.tar.gz" -C package "transcendent-${VERSION}"

echo "Package created: transcendent-${VERSION}.tar.gz"