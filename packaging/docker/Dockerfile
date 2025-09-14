# Multi-stage Dockerfile for Transcendent application

# Build stage
FROM ubuntu:22.04 AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    git \
    libssl-dev \
    libpq-dev \
    openjdk-11-jdk \
    python3 \
    python3-pip \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Bazel
RUN wget -O /tmp/bazel-installer.sh https://github.com/bazelbuild/bazel/releases/download/6.0.0/bazel-6.0.0-installer-linux-x86_64.sh \
    && chmod +x /tmp/bazel-installer.sh \
    && /tmp/bazel-installer.sh \
    && rm /tmp/bazel-installer.sh

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Build the application
RUN bazel build //src/main/cpp:transcendent

# Runtime stage
FROM ubuntu:22.04 AS runtime

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    libssl3 \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Create application user
RUN useradd -r -s /bin/false -d /app transcendent

# Set working directory
WORKDIR /app

# Copy binary from build stage
COPY --from=builder /app/bazel-bin/src/main/cpp/transcendent ./transcendent

# Copy configuration files
COPY --from=builder /app/config/environments/production/ ./config/

# Create log directory
RUN mkdir -p /var/log/transcendent && \
    chown transcendent:transcendent /var/log/transcendent

# Switch to application user
USER transcendent

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Expose port
EXPOSE 8080

# Start the application
CMD ["./transcendent", "--config=./config/application.conf"]