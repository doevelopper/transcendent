#pragma once

class TestFixtures {
public:
    static void setupDatabase();
    static void cleanupDatabase();
    static void createTestUsers();
    static void removeTestUsers();
};