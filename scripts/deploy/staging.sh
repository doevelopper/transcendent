#!/bin/bash
# Deploy to staging environment

set -e

ENVIRONMENT="staging"

echo "Deploying to ${ENVIRONMENT} environment..."

# Build and package
./scripts/build/build.sh
./scripts/build/package.sh

# Deploy using Kubernetes
kubectl apply -f deployment/kubernetes/staging/

# Wait for deployment
kubectl rollout status deployment/transcendent -n staging

echo "Deployment to ${ENVIRONMENT} completed successfully!"