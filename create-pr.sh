#!/bin/bash

# GitHub REST API Pull Request Creation Script
# This script creates a pull request from feature branch to main branch

# Configuration - these should be provided by the user
REPO_OWNER="your-repo-owner"
REPO_NAME="your-repo-name"

# Environment variables for authentication
GITHUB_TOKEN="${GITHUB_TOKEN:-$GITHUB_AUTH_TOKEN}"

# If no token is provided, exit with error
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: GitHub token not found. Please set GITHUB_TOKEN environment variable."
    exit 1
fi

# Branch names
BASE_BRANCH="main"
HEAD_BRANCH="feature/customer-cart-flow-chart"

# Pull request title and description
PR_TITLE="Add customer cart flow chart"
PR_DESCRIPTION="This PR introduces the customer cart flow chart based on the requirements."

# API endpoint
API_URL="https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/pulls"

# Create the pull request
echo "Creating pull request from $HEAD_BRANCH to $BASE_BRANCH..."
echo "API URL: $API_URL"

curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token $GITHUB_TOKEN" \
  -d '{
    "title": "'"$PR_TITLE"'",
    "head": "'"$HEAD_BRANCH"'",
    "base": "'"$BASE_BRANCH"'",
    "body": "'"$PR_DESCRIPTION"'"
  }' \
  "$API_URL"

echo -e "\nPull request creation attempt completed."