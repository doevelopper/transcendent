#!/bin/bash
# Cross-compile script for Transcendent application

set -e

TARGET_PLATFORM=${1:-"linux_x86_64"}

echo "Cross-compiling for platform: ${TARGET_PLATFORM}"

case "${TARGET_PLATFORM}" in
    "linux_x86_64")
        bazel build --platforms=//config/bazel/platforms:linux_x86_64 //src/main/cpp:transcendent
        ;;
    "darwin_x86_64")
        bazel build --platforms=//config/bazel/platforms:darwin_x86_64 //src/main/cpp:transcendent
        ;;
    "windows_x86_64")
        bazel build --platforms=//config/bazel/platforms:windows_x86_64 //src/main/cpp:transcendent
        ;;
    *)
        echo "Unsupported platform: ${TARGET_PLATFORM}"
        echo "Supported platforms: linux_x86_64, darwin_x86_64, windows_x86_64"
        exit 1
        ;;
esac

echo "Cross-compilation completed for ${TARGET_PLATFORM}!"