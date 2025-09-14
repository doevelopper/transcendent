#include <cucumber-cpp/cucumber-cpp.hpp>
#include <regex>

using cucumber::ScenarioScope;

GIVEN("^the validation system is active$") {
    ScenarioScope<Context> context;
    context->validationActive = true;
}

WHEN("^I validate email \"([^\"]*)\"$") {
    REGEX_PARAM(std::string, email);
    
    ScenarioScope<Context> context;
    // Simple email validation regex
    std::regex emailRegex(R"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})");
    context->validationResult = std::regex_match(email, emailRegex);
}

THEN("^the validation should pass$") {
    ScenarioScope<Context> context;
    EXPECT_TRUE(context->validationResult);
}