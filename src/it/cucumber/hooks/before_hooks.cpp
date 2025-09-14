#include <cucumber-cpp/cucumber-cpp.hpp>
#include "../support/TestFixtures.hpp"

BEFORE() {
    TestFixtures::setupDatabase();
    TestFixtures::createTestUsers();
}