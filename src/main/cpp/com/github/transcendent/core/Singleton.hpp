#pragma once

namespace github::transcendent::core {
    template<typename T>
    class Singleton {
    public:
        static T& getInstance();
    private:
        Singleton() = default;
    };
}