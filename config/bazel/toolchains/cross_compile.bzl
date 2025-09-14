"""Cross-compilation toolchain configuration."""

def _cross_compile_toolchain_impl(ctx):
    """Implementation of cross_compile_toolchain rule."""
    return [platform_common.ToolchainInfo(
        target_arch = ctx.attr.target_arch,
        target_os = ctx.attr.target_os,
        cross_compiler = ctx.attr.cross_compiler,
    )]

cross_compile_toolchain = rule(
    implementation = _cross_compile_toolchain_impl,
    attrs = {
        "target_arch": attr.string(mandatory = True),
        "target_os": attr.string(mandatory = True),
        "cross_compiler": attr.string(mandatory = True),
    },
)