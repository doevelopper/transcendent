"""Behave rules for Bazel."""

def _behave_test_impl(ctx):
    """Implementation of behave_test rule."""
    executable = ctx.actions.declare_file(ctx.label.name)
    
    ctx.actions.write(
        output = executable,
        content = """#!/bin/bash
set -e
echo "Running Behave tests"
export PYTHONPATH=$PYTHONPATH:{pythonpath}
{behave_executable} {features}
""".format(
            behave_executable = ctx.attr.behave_executable,
            features = " ".join([f.path for f in ctx.files.features]),
            pythonpath = ":".join([f.dirname for f in ctx.files.steps]),
        ),
        is_executable = True,
    )
    
    return [DefaultInfo(executable = executable)]

behave_test = rule(
    implementation = _behave_test_impl,
    attrs = {
        "features": attr.label_list(allow_files = [".feature"]),
        "steps": attr.label_list(allow_files = [".py"]),
        "behave_executable": attr.string(default = "behave"),
    },
    test = True,
)