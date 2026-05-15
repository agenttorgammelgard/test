# Git Workflow Guide

## Creating Feature Branches

### Branch Naming Conventions
- Use lowercase letters, numbers, and hyphens only
- Be descriptive and concise
- Include issue number when applicable
- Examples:
  - `feat/user-login`
  - `fix/broken-link`
  - `refactor/database-connection`
  - `docs/update-readme`

### Creating a Branch
```bash
# Create and switch to new branch
git checkout -b feat/user-login

# Or using git switch (Git 2.23+)
git switch -c feat/user-login
```

## Committing Changes

### Best Practices
- Make small, focused commits
- Write clear, descriptive commit messages
- Follow the conventional commit format:
  - `feat: add new user authentication`
  - `fix: resolve login button crash`
  - `docs: update API documentation`
  - `refactor: optimize database queries`

### Commit Message Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

## Pull Request Process

### PR Description Template
```
## Summary
Brief description of what this PR does

## Changes
- List of key changes
- Related issues fixed

## Testing
How this was tested
```

### Review Process
1. Request review from team members
2. Address feedback
3. Squash commits if needed
4. Merge to main branch