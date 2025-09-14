#!/bin/bash
# Clean script for Transcendent application

set -e

echo "Cleaning Transcendent application..."

# Clean Bazel outputs
bazel clean --expunge

# Remove generated files
find . -name "*.log" -delete
find . -name "core.*" -delete
find . -name "*.tmp" -delete

# Clean Docker containers and images
docker system prune -f

echo "Clean completed successfully!"