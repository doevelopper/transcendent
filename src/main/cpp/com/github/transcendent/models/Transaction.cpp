#include "Transaction.hpp"

namespace github::transcendent::models {
    Transaction::Transaction() : amount_(0.0) {}

    Transaction::Transaction(const std::string& id, double amount, const std::string& type) 
        : id_(id), amount_(amount), type_(type) {}

    std::string Transaction::getId() const { return id_; }
    void Transaction::setId(const std::string& id) { id_ = id; }

    double Transaction::getAmount() const { return amount_; }
    void Transaction::setAmount(double amount) { amount_ = amount; }

    std::string Transaction::getType() const { return type_; }
    void Transaction::setType(const std::string& type) { type_ = type; }

    std::string Transaction::getTimestamp() const { return timestamp_; }
    void Transaction::setTimestamp(const std::string& timestamp) { timestamp_ = timestamp; }
}