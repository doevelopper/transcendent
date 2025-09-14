#pragma once
#include <string>

namespace github::transcendent::services {
    class NetworkService {
    public:
        bool sendRequest(const std::string& url, const std::string& data);
        std::string receiveResponse();
        bool isConnected();
        void connect(const std::string& endpoint);
        void disconnect();
    };
}