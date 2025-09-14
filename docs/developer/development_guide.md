# Transcendent Developer Guide

## Development Environment Setup

### Prerequisites

- **C++ Compiler**: GCC 9+ or Clang 10+
- **Bazel**: Build system (version 6.0+)
- **Docker**: For containerized development
- **Git**: Version control
- **IDE**: Recommended: CLion, VS Code with C++ extensions

### Setting Up the Development Environment

1. **Clone the repository**:
```bash
git clone https://github.com/yourorg/transcendent.git
cd transcendent
```

2. **Install dependencies**:
```bash
# Install Bazel (Ubuntu/Debian)
sudo apt install bazel

# Or using Homebrew (macOS)
brew install bazel
```

3. **Build the project**:
```bash
./scripts/build/build.sh
```

4. **Run tests**:
```bash
./scripts/test/unit_test.sh
./scripts/test/integration_test.sh
```

## Project Structure

```
transcendent/
├── src/
│   ├── main/cpp/           # Main application source
│   ├── test/cpp/           # Unit tests
│   └── it/                 # Integration tests
├── config/                 # Configuration files
├── scripts/                # Build and deployment scripts
├── docs/                   # Documentation
└── BUILD.bazel            # Root build file
```

## Coding Standards

### C++ Style Guide

We follow the Google C++ Style Guide with some modifications:

1. **Naming Conventions**:
   - Classes: `PascalCase` (e.g., `UserService`)
   - Functions: `camelCase` (e.g., `getUserById`)
   - Variables: `snake_case` (e.g., `user_id`)
   - Constants: `kCamelCase` (e.g., `kMaxRetries`)

2. **File Organization**:
   - Header files: `.hpp` extension
   - Source files: `.cpp` extension
   - One class per file
   - Header guards: `#pragma once`

3. **Documentation**:
   - All public APIs must have Doxygen comments
   - Complex algorithms need inline comments
   - README files for each module

### Example Code Structure

```cpp
// user_service.hpp
#pragma once

#include <memory>
#include <string>
#include <vector>

namespace github::transcendent::services {

/**
 * @brief Service for managing user operations
 */
class UserService {
public:
    /**
     * @brief Create a new user
     * @param username The username for the new user
     * @param email The email address
     * @return User ID if successful, -1 if failed
     */
    int createUser(const std::string& username, const std::string& email);
    
    /**
     * @brief Retrieve user by ID
     * @param user_id The unique user identifier
     * @return User object or nullptr if not found
     */
    std::unique_ptr<User> getUserById(int user_id) const;

private:
    // Implementation details...
};

} // namespace github::transcendent::services
```

## Build System

### Bazel Basics

The project uses Bazel for building, testing, and packaging:

```bash
# Build the main application
bazel build //src/main/cpp:transcendent

# Run specific tests
bazel test //src/test/cpp:user_service_test

# Run all tests
bazel test //...

# Build with optimizations
bazel build -c opt //src/main/cpp:transcendent
```

### Adding New Dependencies

1. **Add to WORKSPACE file**:
```python
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "new_dependency",
    urls = ["https://github.com/example/repo/archive/v1.0.0.tar.gz"],
    sha256 = "...",
    strip_prefix = "repo-1.0.0",
)
```

2. **Use in BUILD.bazel**:
```python
cc_library(
    name = "my_library",
    srcs = ["my_file.cpp"],
    hdrs = ["my_file.hpp"],
    deps = [
        "@new_dependency//path/to/target",
    ],
)
```

## Testing

### Unit Testing with Google Test

```cpp
#include <gtest/gtest.h>
#include "user_service.hpp"

namespace github::transcendent::services {

class UserServiceTest : public ::testing::Test {
protected:
    void SetUp() override {
        service = std::make_unique<UserService>();
    }
    
    std::unique_ptr<UserService> service;
};

TEST_F(UserServiceTest, CreateUserSuccess) {
    int user_id = service->createUser("testuser", "test@example.com");
    EXPECT_GT(user_id, 0);
}

TEST_F(UserServiceTest, GetUserById) {
    int user_id = service->createUser("testuser", "test@example.com");
    auto user = service->getUserById(user_id);
    ASSERT_NE(user, nullptr);
    EXPECT_EQ(user->getUsername(), "testuser");
}

} // namespace github::transcendent::services
```

### Integration Testing with Cucumber

Feature files describe behavior in business terms:

```gherkin
# features/user_management.feature
Feature: User Management
  As a system administrator
  I want to manage users
  So that I can control access to the system

  Scenario: Create a new user
    Given the system is running
    When I create a user with username "testuser" and email "test@example.com"
    Then the user should be created successfully
    And I should be able to retrieve the user by ID
```

Step definitions implement the test logic:

```cpp
#include <cucumber-cpp/defs.hpp>
#include "user_service.hpp"

GIVEN("^the system is running$") {
    // Setup test environment
}

WHEN("^I create a user with username \"([^\"]*)\" and email \"([^\"]*)\"$") {
    REGEX_PARAM(std::string, username);
    REGEX_PARAM(std::string, email);
    
    user_id = user_service->createUser(username, email);
}

THEN("^the user should be created successfully$") {
    EXPECT_GT(user_id, 0);
}
```

## Debugging

### Using GDB with Bazel

```bash
# Build with debug information
bazel build -c dbg //src/main/cpp:transcendent

# Run with GDB
gdb bazel-bin/src/main/cpp/transcendent
```

### Logging

Use the centralized logging system:

```cpp
#include "logging/logger.hpp"

void someFunction() {
    LOG_INFO("Processing user request");
    LOG_DEBUG("User ID: {}", user_id);
    LOG_ERROR("Failed to process request: {}", error_message);
}
```

## Performance Optimization

### Profiling

1. **Build with profiling**:
```bash
bazel build -c opt --copt=-pg //src/main/cpp:transcendent
```

2. **Run and generate profile**:
```bash
./bazel-bin/src/main/cpp/transcendent
gprof ./bazel-bin/src/main/cpp/transcendent gmon.out > profile.txt
```

### Memory Management

- Use smart pointers (`std::unique_ptr`, `std::shared_ptr`)
- Follow RAII principles
- Use memory pools for frequent allocations
- Profile with Valgrind or AddressSanitizer

## Contributing

### Workflow

1. **Create feature branch**:
```bash
git checkout -b feature/new-feature
```

2. **Make changes and test**:
```bash
./scripts/build/build.sh
./scripts/test/unit_test.sh
```

3. **Commit and push**:
```bash
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

4. **Create pull request**

### Code Review Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Performance impact considered
- [ ] Security implications reviewed

## Deployment

### Development Deployment

```bash
./scripts/deploy/dev.sh
```

### Production Deployment

```bash
./scripts/deploy/prod.sh v1.2.3
```

## Troubleshooting

### Common Build Issues

**Bazel cache issues**:
```bash
bazel clean --expunge
```

**Missing dependencies**:
```bash
bazel query --output=build //target:name
```

**Compilation errors**:
- Check C++ standard compatibility
- Verify include paths
- Check namespace usage