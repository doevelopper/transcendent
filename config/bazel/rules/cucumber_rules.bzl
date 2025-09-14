"""Cucumber-cpp rules for Bazel."""

def _cucumber_test_impl(ctx):
    """Implementation of cucumber_test rule."""
    executable = ctx.actions.declare_file(ctx.label.name)
    
    ctx.actions.write(
        output = executable,
        content = """#!/bin/bash
set -e
echo "Running Cucumber-cpp tests"
{cucumber_executable} {features}
""".format(
            cucumber_executable = ctx.attr.cucumber_executable,
            features = " ".join([f.path for f in ctx.files.features]),
        ),
        is_executable = True,
    )
    
    return [DefaultInfo(executable = executable)]

cucumber_test = rule(
    implementation = _cucumber_test_impl,
    attrs = {
        "features": attr.label_list(allow_files = [".feature"]),
        "step_definitions": attr.label_list(allow_files = [".cpp", ".hpp"]),
        "cucumber_executable": attr.string(default = "cucumber-cpp"),
    },
    test = True,
)