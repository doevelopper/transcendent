#!/bin/bash
# Deploy to development environment

set -e

ENVIRONMENT="development"

echo "Deploying to ${ENVIRONMENT} environment..."

# Build the application
./scripts/build/build.sh

# Deploy using Docker Compose
docker-compose -f deployment/docker/docker-compose.dev.yml up -d

echo "Deployment to ${ENVIRONMENT} completed successfully!"
echo "Application is running at: http://localhost:8080"