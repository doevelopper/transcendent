#pragma once
#include <string>

namespace github::transcendent::models {
    class Transaction {
    public:
        Transaction();
        Transaction(const std::string& id, double amount, const std::string& type);
        
        std::string getId() const;
        void setId(const std::string& id);
        
        double getAmount() const;
        void setAmount(double amount);
        
        std::string getType() const;
        void setType(const std::string& type);
        
        std::string getTimestamp() const;
        void setTimestamp(const std::string& timestamp);
        
    private:
        std::string id_;
        double amount_;
        std::string type_;
        std::string timestamp_;
    };
}