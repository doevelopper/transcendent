# Cucumber-cpp

Behavior-Driven Development framework for C++.

## Version

This directory contains build configuration for cucumber-cpp integration with Bazel.

## Usage

Include in your test targets:

```python
cc_test(
    name = "integration_test",
    srcs = ["integration_test.cpp"],
    deps = [
        "//third_party/cucumber_cpp",
        # other dependencies
    ],
)
```