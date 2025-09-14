#!/bin/bash
# Build script for Transcendent application

set -e

echo "Building Transcendent application..."

# Clean previous builds
echo "Cleaning previous builds..."
bazel clean

# Build the application
echo "Building with Bazel..."
bazel build //src/main/cpp:transcendent

# Build tests
echo "Building tests..."
bazel build //src/test/...

echo "Build completed successfully!"
echo "Binary location: bazel-bin/src/main/cpp/transcendent"