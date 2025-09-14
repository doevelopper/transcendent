#!/bin/bash
# Database backup script

set -e

BACKUP_DIR="/var/backups/transcendent"
DATE=$(date +%Y%m%d_%H%M%S)
DATABASE_NAME="transcendent_db"

echo "Starting database backup..."

# Create backup directory
mkdir -p "${BACKUP_DIR}"

# Perform backup
pg_dump "${DATABASE_NAME}" > "${BACKUP_DIR}/transcendent_${DATE}.sql"

# Compress backup
gzip "${BACKUP_DIR}/transcendent_${DATE}.sql"

# Clean old backups (keep last 7 days)
find "${BACKUP_DIR}" -name "*.sql.gz" -mtime +7 -delete

echo "Database backup completed: transcendent_${DATE}.sql.gz"