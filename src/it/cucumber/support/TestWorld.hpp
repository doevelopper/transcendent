#pragma once
#include "../../../../main/cpp/com/github/transcendent/models/User.hpp"
#include "../../../../main/cpp/com/github/transcendent/models/Transaction.hpp"

struct Context {
    bool systemRunning = false;
    bool userCreated = false;
    bool hasUserAccount = false;
    bool transactionProcessed = false;
    bool validationActive = false;
    bool validationResult = false;
    
    github::transcendent::models::User user;
    github::transcendent::models::Transaction transaction;
};

class TestWorld {
public:
    void setup();
    void teardown();
    Context* getContext();
    
private:
    Context context_;
};