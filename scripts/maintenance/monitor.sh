#!/bin/bash
# System monitoring script

set -e

echo "=== System Status Report ==="
echo "Date: $(date)"
echo

# CPU Usage
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)" | awk '{print $2}' | awk -F'%' '{print $1"%"}'
echo

# Memory Usage
echo "Memory Usage:"
free -h | grep -E "^Mem"
echo

# Disk Usage
echo "Disk Usage:"
df -h / | tail -1
echo

# Application Status
echo "Application Status:"
if pgrep -f transcendent > /dev/null; then
    echo "✓ Application is running"
    echo "Process count: $(pgrep -f transcendent | wc -l)"
else
    echo "✗ Application is not running"
fi
echo

# Database Status
echo "Database Status:"
if pg_isready -q; then
    echo "✓ Database is accessible"
else
    echo "✗ Database is not accessible"
fi
echo

# Network Status
echo "Network Status:"
if curl -s http://localhost:8080/health > /dev/null; then
    echo "✓ Application health endpoint is responding"
else
    echo "✗ Application health endpoint is not responding"
fi