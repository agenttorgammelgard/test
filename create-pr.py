#!/usr/bin/env python3
"""
GitHub REST API Pull Request Creation Script
Uses Git credential store for authentication - no hardcoded tokens
"""

import os
import sys
import subprocess
import requests
import json

def get_github_token_from_git():
    """Get GitHub token from Git credential store"""
    try:
        # Run git credential fill to get stored credentials
        result = subprocess.run(
            ['git', 'credential', 'fill'],
            input='protocol=https\nhost=github.com\n',
            text=True,
            capture_output=True,
            check=True
        )
        
        # Parse the output to extract credentials
        output = result.stdout
        username = None
        password = None
        
        for line in output.split('\n'):
            if line.startswith('username='):
                username = line.split('=', 1)[1]
            elif line.startswith('password='):
                password = line.split('=', 1)[1]
        
        if not username or not password:
            raise ValueError("No credentials found in Git credential store")
        
        return password  # The password field contains the GitHub token
        
    except subprocess.CalledProcessError as e:
        print(f"Error calling git credential: {e.stderr}", file=sys.stderr)
        raise
    except Exception as e:
        print(f"Error retrieving GitHub credentials: {e}", file=sys.stderr)
        raise

def create_pull_request():
    # Configuration - these should be provided by the user
    repo_owner = "agenttorgammelgard"  # Replace with actual owner
    repo_name = "test"    # Replace with actual repo name
    
    # Get GitHub token from Git credential store
    github_token = get_github_token_from_git()
    
    # Branch names
    base_branch = "main"
    head_branch = "new-branch"
    
    # Pull request title and description
    pr_title = "Add hello.txt with hello world content"
    pr_description = "This PR adds hello.txt containing hello world message."
    
    # API endpoint
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    
    # Headers
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {github_token}"
    }
    
    # Payload
    payload = {
        "title": pr_title,
        "head": head_branch,
        "base": base_branch,
        "body": pr_description
    }
    
    print(f"Creating pull request from {head_branch} to {base_branch}")
    print(f"API URL: {api_url}")
    print(f"Using Git credential store for authentication")
    
    try:
        # Make the API call
        response = requests.post(api_url, headers=headers, json=payload)
        
        # Check response
        if response.status_code == 201:
            print("Pull request created successfully!")
            pr_data = response.json()
            print(f"PR Number: {pr_data['number']}")
            print(f"PR URL: {pr_data['html_url']}")
            return True
        else:
            print(f"Failed to create pull request. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return False

if __name__ == "__main__":
    success = create_pull_request()
    if not success:
        sys.exit(1)
