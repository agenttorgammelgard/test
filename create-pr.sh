#!/bin/bash

# GitHub REST API Pull Request Creation Script
# This script creates a pull request from feature branch to main branch
# Uses Git credential store for authentication - no hardcoded tokens

# Configuration - these should be provided by the user
REPO_OWNER="agenttorgammelgard"
REPO_NAME="test"

# Get credentials from Git credential store
get_git_credentials() {
    local host="${1:-github.com}"
    local protocol="${2:-https}"
    
    # Use git credential fill to retrieve stored credentials
    local creds=$(git credential fill <<< "protocol=$protocol\nhost=$host\n")
    
    # Extract username and password/token
    local username=$(echo "$creds" | grep "^username=" | cut -d= -f2-)
    local password=$(echo "$creds" | grep "^password=" | cut -d= -f2-)
    
    if [ -z "$username" ] || [ -z "$password" ]; then
        echo "Error: No credentials found in Git credential store for $host" >&2
        return 1
    fi
    
    # Return as colon-separated username:password (token)
    echo "$username:$password"
}

# Get GitHub credentials from Git credential store
GITHUB_CREDS=$(get_git_credentials "github.com" "https")

if [ -z "$GITHUB_CREDS" ]; then
    echo "Error: Failed to retrieve GitHub credentials from Git credential store." >&2
    exit 1
fi

# Extract token (second field)
GITHUB_TOKEN=$(echo "$GITHUB_CREDS" | cut -d: -f2-)

# Branch names
BASE_BRANCH="main"
HEAD_BRANCH="new-branch"

# Pull request title and description
PR_TITLE="Add hello.txt with hello world content"
PR_DESCRIPTION="This PR adds hello.txt containing hello world message."

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
