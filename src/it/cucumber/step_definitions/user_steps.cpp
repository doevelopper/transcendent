#include <cucumber-cpp/cucumber-cpp.hpp>
#include "../../../../main/cpp/com/github/transcendent/models/User.hpp"
#include "../../../../main/cpp/com/github/transcendent/services/DataService.hpp"

using cucumber::ScenarioScope;

GIVEN("^the system is running$") {
    ScenarioScope<Context> context;
    context->systemRunning = true;
}

WHEN("^I create a user with username \"([^\"]*)\" and email \"([^\"]*)\"$") {
    REGEX_PARAM(std::string, username);
    REGEX_PARAM(std::string, email);
    
    ScenarioScope<Context> context;
    context->user = github::transcendent::models::User(username, email);
    context->userCreated = true;
}

THEN("^the user should be created successfully$") {
    ScenarioScope<Context> context;
    EXPECT_TRUE(context->userCreated);
}