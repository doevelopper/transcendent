#pragma once
#include <string>

namespace github::transcendent::logging {
    enum class LogLevel {
        DEBUG, INFO, WARN, ERROR
    };

    class Logger {
    public:
        static Logger& getInstance();
        void log(LogLevel level, const std::string& message);
        void debug(const std::string& message);
        void info(const std::string& message);
        void warn(const std::string& message);
        void error(const std::string& message);
    };
}