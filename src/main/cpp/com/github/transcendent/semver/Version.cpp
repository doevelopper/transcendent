#include "Version.hpp"
#include <sstream>

namespace github::transcendent::semver {
    Version::Version(int major, int minor, int patch) 
        : major_(major), minor_(minor), patch_(patch) {}

    Version::Version(const std::string& version) {
        // Parse version string
        major_ = 1; minor_ = 0; patch_ = 0;
    }

    int Version::getMajor() const { return major_; }
    int Version::getMinor() const { return minor_; }
    int Version::getPatch() const { return patch_; }

    std::string Version::toString() const {
        std::ostringstream oss;
        oss << major_ << "." << minor_ << "." << patch_;
        return oss.str();
    }

    bool Version::operator<(const Version& other) const {
        if (major_ != other.major_) return major_ < other.major_;
        if (minor_ != other.minor_) return minor_ < other.minor_;
        return patch_ < other.patch_;
    }

    bool Version::operator==(const Version& other) const {
        return major_ == other.major_ && minor_ == other.minor_ && patch_ == other.patch_;
    }
}