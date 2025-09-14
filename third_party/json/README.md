# JSON for Modern C++

JSON library for C++ with intuitive syntax.

## Version

This directory contains build configuration for nlohmann/json integration with Bazel.

## Usage

Include in your targets:

```python
cc_library(
    name = "my_library",
    srcs = ["my_library.cpp"],
    deps = [
        "//third_party/json",
        # other dependencies
    ],
)
```

## Example Usage

```cpp
#include <nlohmann/json.hpp>

using json = nlohmann::json;

json data = {
    {"name", "John"},
    {"age", 30}
};

std::string serialized = data.dump();
```