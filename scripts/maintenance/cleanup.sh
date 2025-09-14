#!/bin/bash
# Log cleanup script

set -e

LOG_DIR="/var/log/transcendent"
MAX_AGE_DAYS=30

echo "Cleaning up old log files..."

# Clean application logs older than MAX_AGE_DAYS
if [ -d "${LOG_DIR}" ]; then
    find "${LOG_DIR}" -name "*.log" -mtime +${MAX_AGE_DAYS} -delete
    find "${LOG_DIR}" -name "*.log.*" -mtime +${MAX_AGE_DAYS} -delete
    
    # Compress logs older than 7 days
    find "${LOG_DIR}" -name "*.log" -mtime +7 -not -name "*.gz" -exec gzip {} \;
fi

# Clean Docker logs
docker system prune -f --volumes --filter "until=720h"

# Clean Bazel cache
bazel clean --expunge_async

echo "Log cleanup completed"
echo "Removed logs older than ${MAX_AGE_DAYS} days"