# Google Test

Google's C++ testing framework.

## Version

This directory contains build configuration for Google Test integration with Bazel.

## Usage

Include in your test targets:

```python
cc_test(
    name = "unit_test",
    srcs = ["unit_test.cpp"],
    deps = [
        "//third_party/gtest",
        # other dependencies
    ],
)
```