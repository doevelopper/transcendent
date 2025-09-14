#include "Logger.hpp"
#include <iostream>

namespace github::transcendent::logging {
    Logger& Logger::getInstance() {
        static Logger instance;
        return instance;
    }

    void Logger::log(LogLevel level, const std::string& message) {
        std::cout << "[" << static_cast<int>(level) << "] " << message << std::endl;
    }

    void Logger::debug(const std::string& message) {
        log(LogLevel::DEBUG, message);
    }

    void Logger::info(const std::string& message) {
        log(LogLevel::INFO, message);
    }

    void Logger::warn(const std::string& message) {
        log(LogLevel::WARN, message);
    }

    void Logger::error(const std::string& message) {
        log(LogLevel::ERROR, message);
    }
}