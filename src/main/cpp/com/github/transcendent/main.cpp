#include "launcher/Application.hpp"

int main(int argc, char* argv[]) {
    github::transcendent::launcher::Application app;
    return app.run(argc, argv);
}