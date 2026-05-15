# GitHub Pull Request Creation via REST API

## API Endpoint
```
POST https://api.github.com/repos/{owner}/{repo}/pulls
```

## Headers
```
Accept: application/vnd.github.v3+json
Authorization: token {github_token}
```

## Request Body
```json
{
  "title": "Add customer cart flow chart",
  "head": "feature/customer-cart-flow-chart",
  "base": "main",
  "body": "This PR introduces the customer cart flow chart based on the requirements."
}
```

## Example cURL Command
```bash
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token $GITHUB_TOKEN" \
  -d '{
    "title": "Add customer cart flow chart",
    "head": "feature/customer-cart-flow-chart",
    "base": "main",
    "body": "This PR introduces the customer cart flow chart based on the requirements."
  }' \
  https://api.github.com/repos/{owner}/{repo}/pulls
```

## Response
Successful creation returns HTTP 201 with PR details:
```json
{
  "id": 123456,
  "number": 789,
  "title": "Add customer cart flow chart",
  "html_url": "https://github.com/{owner}/{repo}/pull/789",
  ...
}
```

## Error Handling
- 401: Unauthorized (invalid token)
- 403: Forbidden (insufficient permissions)
- 422: Validation error (branch names, etc.)
- 404: Repository not found

## Authentication
Set environment variable: `GITHUB_TOKEN` with appropriate permissions for the repository.

## Required Permissions
- `repo` scope for full repository access
- `pull_requests` permissions