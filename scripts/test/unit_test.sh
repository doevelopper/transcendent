#!/bin/bash
# Run unit tests

set -e

echo "Running unit tests..."

# Run C++ unit tests
echo "Running C++ unit tests with Google Test..."
bazel test //src/test/...

echo "Unit tests completed successfully!"