"""Linux x86_64 platform configuration."""

platform(
    name = "linux_x86_64",
    constraint_values = [
        "@platforms//os:linux",
        "@platforms//cpu:x86_64",
    ],
)

# Toolchain configuration for Linux x86_64
toolchain(
    name = "linux_x86_64_toolchain",
    exec_compatible_with = [
        "@platforms//os:linux",
        "@platforms//cpu:x86_64",
    ],
    target_compatible_with = [
        "@platforms//os:linux", 
        "@platforms//cpu:x86_64",
    ],
    toolchain = "//config/bazel/toolchains:cpp_toolchain_linux",
    toolchain_type = "@bazel_tools//tools/cpp:toolchain_type",
)