#pragma once
#include "Version.hpp"
#include <string>

namespace github::transcendent::semver {
    class VersionConstraint {
    public:
        VersionConstraint(const std::string& constraint);
        bool matches(const Version& version) const;
        
    private:
        std::string constraint_;
    };
}