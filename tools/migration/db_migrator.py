#!/usr/bin/env python3
"""
Database migration tool for Transcendent application.
"""

import argparse
import psycopg2
import os
import re
from pathlib import Path
import datetime


class DatabaseMigrator:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.migrations_dir = Path(__file__).parent / "migrations"
        
    def connect(self):
        """Connect to the database."""
        return psycopg2.connect(self.connection_string)
    
    def create_migrations_table(self):
        """Create the migrations tracking table."""
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS schema_migrations (
                        version VARCHAR(14) PRIMARY KEY,
                        applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
    
    def get_applied_migrations(self):
        """Get list of applied migrations."""
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version FROM schema_migrations ORDER BY version")
                return [row[0] for row in cur.fetchall()]
    
    def get_pending_migrations(self):
        """Get list of pending migrations."""
        applied = set(self.get_applied_migrations())
        
        migration_files = sorted([
            f for f in self.migrations_dir.glob("*.sql")
            if re.match(r'\d{14}_.*\.sql', f.name)
        ])
        
        pending = []
        for migration_file in migration_files:
            version = migration_file.stem.split('_')[0]
            if version not in applied:
                pending.append((version, migration_file))
        
        return pending
    
    def apply_migration(self, version, migration_file):
        """Apply a single migration."""
        print(f"Applying migration {version}: {migration_file.name}")
        
        with open(migration_file, 'r') as f:
            sql = f.read()
        
        with self.connect() as conn:
            with conn.cursor() as cur:
                # Execute migration SQL
                cur.execute(sql)
                
                # Record migration as applied
                cur.execute(
                    "INSERT INTO schema_migrations (version) VALUES (%s)",
                    (version,)
                )
                
                conn.commit()
        
        print(f"Migration {version} applied successfully")
    
    def migrate(self):
        """Apply all pending migrations."""
        self.create_migrations_table()
        
        pending = self.get_pending_migrations()
        
        if not pending:
            print("No pending migrations")
            return
        
        print(f"Applying {len(pending)} pending migrations...")
        
        for version, migration_file in pending:
            try:
                self.apply_migration(version, migration_file)
            except Exception as e:
                print(f"Error applying migration {version}: {e}")
                raise
        
        print("All migrations applied successfully")
    
    def rollback(self, target_version=None):
        """Rollback migrations to a specific version."""
        print("Rollback functionality not implemented")
        print("Please implement rollback SQL files for safe rollbacks")
    
    def status(self):
        """Show migration status."""
        self.create_migrations_table()
        
        applied = self.get_applied_migrations()
        pending = self.get_pending_migrations()
        
        print("Migration Status:")
        print(f"Applied migrations: {len(applied)}")
        
        if applied:
            print("\nApplied:")
            for version in applied[-5:]:  # Show last 5
                print(f"  ✓ {version}")
        
        print(f"\nPending migrations: {len(pending)}")
        if pending:
            print("\nPending:")
            for version, migration_file in pending[:5]:  # Show first 5
                print(f"  ○ {version}: {migration_file.name}")
    
    def create_migration(self, name):
        """Create a new migration file."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{name}.sql"
        migration_path = self.migrations_dir / filename
        
        # Create migrations directory if it doesn't exist
        self.migrations_dir.mkdir(parents=True, exist_ok=True)
        
        template = f"""-- Migration: {name}
-- Created: {datetime.datetime.now().isoformat()}

-- Up migration
-- Add your migration SQL here

-- Example:
-- CREATE TABLE example_table (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- Down migration (for rollback)
-- CREATE OR REPLACE FUNCTION rollback_{timestamp}() RETURNS void AS $$
-- BEGIN
--     -- Add rollback SQL here
--     -- DROP TABLE IF EXISTS example_table;
-- END;
-- $$ LANGUAGE plpgsql;
"""
        
        with open(migration_path, 'w') as f:
            f.write(template)
        
        print(f"Created migration: {migration_path}")
        return migration_path


def main():
    parser = argparse.ArgumentParser(description="Database migration tool")
    parser.add_argument("--db-url", required=True, help="Database connection URL")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Migrate command
    subparsers.add_parser("migrate", help="Apply pending migrations")
    
    # Status command
    subparsers.add_parser("status", help="Show migration status")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create new migration")
    create_parser.add_argument("name", help="Migration name")
    
    # Rollback command
    rollback_parser = subparsers.add_parser("rollback", help="Rollback migrations")
    rollback_parser.add_argument("--to", help="Target version to rollback to")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    migrator = DatabaseMigrator(args.db_url)
    
    if args.command == "migrate":
        migrator.migrate()
    elif args.command == "status":
        migrator.status()
    elif args.command == "create":
        migrator.create_migration(args.name)
    elif args.command == "rollback":
        migrator.rollback(args.to)


if __name__ == "__main__":
    main()