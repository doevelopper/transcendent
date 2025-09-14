#!/bin/bash
# System health check script

set -e

HEALTH_REPORT="/tmp/transcendent_health_$(date +%Y%m%d_%H%M%S).txt"

echo "Running comprehensive health check..." | tee "${HEALTH_REPORT}"
echo "Date: $(date)" >> "${HEALTH_REPORT}"
echo "=========================" >> "${HEALTH_REPORT}"

# Check system resources
echo "System Resources:" >> "${HEALTH_REPORT}"
echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')" >> "${HEALTH_REPORT}"
echo "Memory: $(free -m | awk 'NR==2{printf "%.1f%% (%s/%s)", $3*100/$2, $3, $2}')" >> "${HEALTH_REPORT}"
echo "Disk: $(df -h / | awk 'NR==2{print $5 " used"}')" >> "${HEALTH_REPORT}"
echo "" >> "${HEALTH_REPORT}"

# Check application processes
echo "Application Processes:" >> "${HEALTH_REPORT}"
pgrep -fl transcendent >> "${HEALTH_REPORT}" 2>&1 || echo "No transcendent processes found" >> "${HEALTH_REPORT}"
echo "" >> "${HEALTH_REPORT}"

# Check network connectivity
echo "Network Connectivity:" >> "${HEALTH_REPORT}"
if curl -s --max-time 5 http://localhost:8080/health > /dev/null; then
    echo "✓ Health endpoint accessible" >> "${HEALTH_REPORT}"
else
    echo "✗ Health endpoint not accessible" >> "${HEALTH_REPORT}"
fi

# Check database
echo "Database Status:" >> "${HEALTH_REPORT}"
if pg_isready -q -t 5; then
    echo "✓ Database connection OK" >> "${HEALTH_REPORT}"
else
    echo "✗ Database connection failed" >> "${HEALTH_REPORT}"
fi

echo "" >> "${HEALTH_REPORT}"
echo "Health check completed. Report saved to: ${HEALTH_REPORT}"
cat "${HEALTH_REPORT}"