#!/bash
# Rollback deployment

set -e

ENVIRONMENT=${1:-"staging"}
REVISION=${2:-"1"}

echo "Rolling back ${ENVIRONMENT} to revision ${REVISION}..."

case "${ENVIRONMENT}" in
    "staging"|"production")
        helm rollback transcendent "${REVISION}" --namespace "${ENVIRONMENT}"
        ;;
    "development")
        docker-compose -f deployment/docker/docker-compose.dev.yml down
        docker-compose -f deployment/docker/docker-compose.dev.yml up -d
        ;;
    *)
        echo "Unknown environment: ${ENVIRONMENT}"
        echo "Supported environments: development, staging, production"
        exit 1
        ;;
esac

echo "Rollback to revision ${REVISION} completed for ${ENVIRONMENT}!"