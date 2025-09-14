#pragma once
#include <string>
#include <vector>

namespace github::transcendent::services {
    class DataService {
    public:
        bool saveData(const std::string& data);
        std::string loadData(const std::string& id);
        std::vector<std::string> getAllData();
        bool deleteData(const std::string& id);
    };
}