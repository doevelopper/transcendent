#!/bin/bash
# Run all tests and generate coverage report

set -e

echo "Running all tests with coverage..."

# Run tests with coverage
bazel coverage //src/test/... //src/it/cucumber/...

# Generate HTML coverage report
genhtml bazel-out/_coverage/_coverage_report.dat -o coverage_html

echo "Coverage report generated in coverage_html/"
echo "Open coverage_html/index.html in your browser to view the report"