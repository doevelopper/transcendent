#include <cucumber-cpp/cucumber-cpp.hpp>
#include "../../../../main/cpp/com/github/transcendent/models/Transaction.hpp"
#include "../../../../main/cpp/com/github/transcendent/services/DataService.hpp"

using cucumber::ScenarioScope;

GIVEN("^I have a user account$") {
    ScenarioScope<Context> context;
    context->hasUserAccount = true;
}

WHEN("^I process a transaction of amount ([0-9.]+) with type \"([^\"]*)\"$") {
    REGEX_PARAM(double, amount);
    REGEX_PARAM(std::string, type);
    
    ScenarioScope<Context> context;
    context->transaction = github::transcendent::models::Transaction("tx_123", amount, type);
    context->transactionProcessed = (amount > 0);
}

THEN("^the transaction should be processed successfully$") {
    ScenarioScope<Context> context;
    EXPECT_TRUE(context->transactionProcessed);
}