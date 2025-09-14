#pragma once
#include <string>
#include <vector>

namespace github::transcendent::semver {
    class Version {
    public:
        Version(int major, int minor, int patch);
        Version(const std::string& version);
        
        int getMajor() const;
        int getMinor() const;
        int getPatch() const;
        
        std::string toString() const;
        bool operator<(const Version& other) const;
        bool operator==(const Version& other) const;
        
    private:
        int major_, minor_, patch_;
    };
}