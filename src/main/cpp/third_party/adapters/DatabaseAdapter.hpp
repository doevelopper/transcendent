#pragma once
#include <string>
#include <vector>

namespace github::transcendent::third_party::adapters {
    class DatabaseAdapter {
    public:
        bool connect(const std::string& connectionString);
        void disconnect();
        bool execute(const std::string& query);
        std::vector<std::string> select(const std::string& query);
        bool isConnected() const;
        
    private:
        bool connected_;
    };
}