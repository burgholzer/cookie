#include "add.hpp"

#include <gtest/gtest.h>

namespace {{ cookiecutter.namespace }} {

TEST(Add, add) { EXPECT_EQ(add(1, 2), 3); }

} // namespace {{ cookiecutter.namespace }}
