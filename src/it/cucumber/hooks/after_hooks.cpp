#include <cucumber-cpp/cucumber-cpp.hpp>
#include "../support/TestFixtures.hpp"

AFTER() {
    TestFixtures::removeTestUsers();
    TestFixtures::cleanupDatabase();
}