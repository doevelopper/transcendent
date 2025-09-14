#include "User.hpp"

namespace github::transcendent::models {
    User::User() {}

    User::User(const std::string& username, const std::string& email) 
        : username_(username), email_(email) {}

    std::string User::getUsername() const { return username_; }
    void User::setUsername(const std::string& username) { username_ = username; }

    std::string User::getEmail() const { return email_; }
    void User::setEmail(const std::string& email) { email_ = email; }

    std::string User::getId() const { return id_; }
    void User::setId(const std::string& id) { id_ = id; }
}