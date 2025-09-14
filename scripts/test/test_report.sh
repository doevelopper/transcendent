#!/bin/bash
# Generate test reports

set -e

echo "Generating test reports..."

REPORT_DIR="reports"
mkdir -p "${REPORT_DIR}"

# Run tests with XML output
bazel test //src/test/... --test_output=xml

# Copy test results
cp -r bazel-testlogs "${REPORT_DIR}/"

# Generate JUnit-style report
find bazel-testlogs -name "test.xml" -exec cp {} "${REPORT_DIR}/" \;

echo "Test reports generated in ${REPORT_DIR}/"