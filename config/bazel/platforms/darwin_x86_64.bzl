"""Darwin x86_64 platform configuration."""

platform(
    name = "darwin_x86_64",
    constraint_values = [
        "@platforms//os:macos",
        "@platforms//cpu:x86_64",
    ],
)

# Toolchain configuration for Darwin x86_64
toolchain(
    name = "darwin_x86_64_toolchain",
    exec_compatible_with = [
        "@platforms//os:macos",
        "@platforms//cpu:x86_64",
    ],
    target_compatible_with = [
        "@platforms//os:macos",
        "@platforms//cpu:x86_64", 
    ],
    toolchain = "//config/bazel/toolchains:cpp_toolchain_darwin",
    toolchain_type = "@bazel_tools//tools/cpp:toolchain_type",
)