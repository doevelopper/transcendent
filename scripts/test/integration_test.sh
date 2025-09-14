#!/bin/bash
# Run integration tests

set -e

echo "Running integration tests..."

# Run Cucumber integration tests
echo "Running Cucumber-cpp integration tests..."
bazel test //src/it/cucumber:integration_tests

# Run Behave integration tests
echo "Running Python Behave tests..."
cd src/it/behave
python -m behave features/

echo "Integration tests completed successfully!"