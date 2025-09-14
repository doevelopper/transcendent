#pragma once

namespace github::transcendent::launcher {
    class Application {
    public:
        int run(int argc, char* argv[]);
        void initialize();
        void shutdown();
    };
}