"""Packaging rules for Bazel."""

def _package_tar_impl(ctx):
    """Implementation of package_tar rule."""
    tar_file = ctx.actions.declare_file(ctx.label.name + ".tar.gz")
    
    ctx.actions.run_shell(
        outputs = [tar_file],
        inputs = ctx.files.srcs,
        command = """
        tar -czf {output} {inputs}
        """.format(
            output = tar_file.path,
            inputs = " ".join([f.path for f in ctx.files.srcs]),
        ),
    )
    
    return [DefaultInfo(files = depset([tar_file]))]

package_tar = rule(
    implementation = _package_tar_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = True),
    },
)