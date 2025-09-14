#include <gtest/gtest.h>
#include "../../../../main/cpp/com/github/transcendent/core/NoOp.hpp"

namespace github::transcendent::core {
    class SingletonTest : public ::testing::Test {
    protected:
        void SetUp() override {}
        void TearDown() override {}
    };

    TEST_F(SingletonTest, BasicTest) {
        EXPECT_TRUE(true);
    }
}