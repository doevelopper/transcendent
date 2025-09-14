#pragma once
#include <string>

namespace github::transcendent::models {
    class User {
    public:
        User();
        User(const std::string& username, const std::string& email);
        
        std::string getUsername() const;
        void setUsername(const std::string& username);
        
        std::string getEmail() const;
        void setEmail(const std::string& email);
        
        std::string getId() const;
        void setId(const std::string& id);
        
    private:
        std::string id_;
        std::string username_;
        std::string email_;
    };
}