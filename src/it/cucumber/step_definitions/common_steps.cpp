#include <cucumber-cpp/cucumber-cpp.hpp>

using cucumber::ScenarioScope;

GIVEN("^.*$") {
    // Common setup steps
}

WHEN("^.*$") {
    // Common action steps
}

THEN("^.*$") {
    // Common verification steps
}

THEN("^an? (.*) should be (.*)$") {
    REGEX_PARAM(std::string, item);
    REGEX_PARAM(std::string, state);
    
    // Common validation logic
}