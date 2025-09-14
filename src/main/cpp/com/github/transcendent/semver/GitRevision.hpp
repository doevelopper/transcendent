#pragma once
#include <string>

#define GIT_REVISION "undefined"
#define BUILD_DATE "undefined"

namespace github::transcendent::semver {
    extern const char* getGitRevision();
    extern const char* getBuildDate();
}