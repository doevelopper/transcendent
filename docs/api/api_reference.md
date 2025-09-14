# Transcendent API Reference

## Overview

The Transcendent application provides a comprehensive API for managing users, transactions, and system operations.

## Base URL

- Development: `http://localhost:8080/api/v1`
- Staging: `https://staging-api.transcendent.example.com/api/v1`
- Production: `https://api.transcendent.example.com/api/v1`

## Authentication

All API endpoints require authentication using JWT tokens:

```
Authorization: Bearer <jwt_token>
```

## Core Endpoints

### Users

#### GET /users
Retrieve a list of all users.

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "username": "john_doe",
      "email": "john@example.com",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

#### POST /users
Create a new user.

**Request:**
```json
{
  "username": "new_user",
  "email": "user@example.com",
  "password": "secure_password"
}
```

#### GET /users/{id}
Retrieve a specific user by ID.

#### PUT /users/{id}
Update an existing user.

#### DELETE /users/{id}
Delete a user.

### Transactions

#### GET /transactions
Retrieve a list of transactions.

#### POST /transactions
Create a new transaction.

#### GET /transactions/{id}
Retrieve a specific transaction.

### Health

#### GET /health
Application health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00Z",
  "version": "1.0.0"
}
```

## Error Handling

All errors follow a consistent format:

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "The request is invalid",
    "details": "Field 'username' is required"
  }
}
```

## Rate Limiting

API requests are limited to:
- 1000 requests per hour for authenticated users
- 100 requests per hour for unauthenticated requests