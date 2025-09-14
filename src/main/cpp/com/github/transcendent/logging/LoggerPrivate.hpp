#pragma once

namespace github::transcendent::logging {
    class LoggerPrivate {
    public:
        void configureLogger();
        void setLogLevel(int level);
    };
}