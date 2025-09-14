# Abseil

Google's collection of C++ common libraries.

## Version

This directory contains build configuration for Abseil integration with Bazel.

## Usage

Include specific Abseil libraries in your targets:

```python
cc_library(
    name = "my_library",
    srcs = ["my_library.cpp"],
    deps = [
        "//third_party/abseil:strings",
        "//third_party/abseil:status",
        # other dependencies
    ],
)
```