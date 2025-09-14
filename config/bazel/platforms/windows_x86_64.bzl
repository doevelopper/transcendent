"""Windows x86_64 platform configuration."""

platform(
    name = "windows_x86_64",
    constraint_values = [
        "@platforms//os:windows",
        "@platforms//cpu:x86_64",
    ],
)

# Toolchain configuration for Windows x86_64
toolchain(
    name = "windows_x86_64_toolchain",
    exec_compatible_with = [
        "@platforms//os:windows",
        "@platforms//cpu:x86_64",
    ],
    target_compatible_with = [
        "@platforms//os:windows",
        "@platforms//cpu:x86_64",
    ],
    toolchain = "//config/bazel/toolchains:cpp_toolchain_windows",
    toolchain_type = "@bazel_tools//tools/cpp:toolchain_type",
)