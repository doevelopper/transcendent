#pragma once
#include <gtest/gtest.h>

namespace github::transcendent::core {
    class SingletonTest : public ::testing::Test {
    protected:
        void SetUp() override;
        void TearDown() override;
    };
}