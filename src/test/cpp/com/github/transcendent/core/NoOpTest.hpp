#pragma once
#include <gtest/gtest.h>
#include "../../../../main/cpp/com/github/transcendent/core/NoOp.hpp"

namespace github::transcendent::core {
    class NoOpTest : public ::testing::Test {
    protected:
        void SetUp() override;
        void TearDown() override;
        NoOp noOp;
    };
}