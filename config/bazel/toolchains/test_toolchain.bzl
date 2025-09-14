"""Test toolchain configuration for Bazel."""

def _test_toolchain_impl(ctx):
    """Implementation of test_toolchain rule."""
    return [platform_common.ToolchainInfo(
        test_runner = ctx.attr.test_runner,
        test_env = ctx.attr.test_env,
    )]

test_toolchain = rule(
    implementation = _test_toolchain_impl,
    attrs = {
        "test_runner": attr.string(mandatory = True),
        "test_env": attr.string_dict(default = {}),
    },
)