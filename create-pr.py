#!/usr/bin/env python3
"""
GitHub REST API Pull Request Creation Script
"""

import os
import sys
import requests
import json

def create_pull_request():
    # Configuration - these should be provided by the user
    repo_owner = "your-repo-owner"  # Replace with actual owner
    repo_name = "your-repo-name"    # Replace with actual repo name
    
    # Get GitHub token from environment
    github_token = os.environ.get('GITHUB_TOKEN') or os.environ.get('GITHUB_AUTH_TOKEN')
    
    if not github_token:
        print("Error: GitHub token not found. Please set GITHUB_TOKEN or GITHUB_AUTH_TOKEN environment variable.")
        return False
    
    # Branch names
    base_branch = "main"
    head_branch = "feature/customer-cart-flow-chart"
    
    # Pull request title and description
    pr_title = "Add customer cart flow chart"
    pr_description = "This PR introduces the customer cart flow chart based on the requirements."
    
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