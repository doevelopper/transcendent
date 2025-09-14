#!/bin/bash
# Deploy to production environment

set -e

ENVIRONMENT="production"
VERSION=${1:-$(date +%Y%m%d-%H%M%S)}

echo "Deploying version ${VERSION} to ${ENVIRONMENT} environment..."

# Confirmation prompt
read -p "Are you sure you want to deploy to production? (y/N): " confirm
if [[ $confirm != [yY] ]]; then
    echo "Deployment cancelled."
    exit 1
fi

# Build and package with version tag
./scripts/build/build.sh
./scripts/build/package.sh "${VERSION}"

# Deploy using Helm
helm upgrade --install transcendent deployment/helm/transcendent \
    --namespace production \
    --set image.tag="${VERSION}" \
    --wait

echo "Deployment to ${ENVIRONMENT} completed successfully!"
echo "Version ${VERSION} is now live"