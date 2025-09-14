"""C++ rules for Bazel."""

def _cpp_binary_impl(ctx):
    """Implementation of cpp_binary rule."""
    output = ctx.actions.declare_file(ctx.label.name)
    
    ctx.actions.run(
        outputs = [output],
        inputs = ctx.files.srcs + ctx.files.deps,
        executable = ctx.attr._cpp_compiler.files_to_run.executable,
        arguments = [
            "-o", output.path,
        ] + [src.path for src in ctx.files.srcs],
    )
    
    return [DefaultInfo(executable = output)]

cpp_binary_extended = rule(
    implementation = _cpp_binary_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = [".cpp", ".cc"]),
        "deps": attr.label_list(),
        "_cpp_compiler": attr.label(default = "@bazel_tools//tools/cpp:toolchain"),
    },
    executable = True,
)