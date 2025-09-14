"""C++ toolchain configuration for Bazel."""

def _cpp_toolchain_impl(ctx):
    """Implementation of cpp_toolchain rule."""
    return [platform_common.ToolchainInfo(
        compiler_path = ctx.attr.compiler_path,
        linker_path = ctx.attr.linker_path,
        ar_path = ctx.attr.ar_path,
        strip_path = ctx.attr.strip_path,
    )]

cpp_toolchain = rule(
    implementation = _cpp_toolchain_impl,
    attrs = {
        "compiler_path": attr.string(mandatory = True),
        "linker_path": attr.string(mandatory = True),
        "ar_path": attr.string(mandatory = True),
        "strip_path": attr.string(mandatory = True),
    },
)