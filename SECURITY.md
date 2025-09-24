# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| 0.1.x   | :x:                |

## Reporting a Vulnerability

We take the security of QuteWindow seriously. If you believe you've found a security vulnerability, please follow these steps:

### How to Report

1. **Do not** create a public GitHub issue for security vulnerabilities
2. **Email** us directly at: parhamoyan@yahoo.com
3. **Include** "Security Vulnerability" in the subject line
4. **Provide** as much detail as possible about the vulnerability

### What to Include

Please include the following information in your report:

- **Description**: A detailed description of the vulnerability
- **Steps to Reproduce**: Clear steps to reproduce the issue
- **Affected Versions**: Which versions are affected
- **Impact**: The potential impact of the vulnerability
- **Suggested Fix**: If available, a suggested fix or mitigation

### What Happens Next

1. **Acknowledgment**: We will acknowledge receipt of your report within 48 hours
2. **Assessment**: We will assess the vulnerability and determine its severity
3. **Resolution**: We will work on a fix and coordinate a release schedule
4. **Disclosure**: We will publicly disclose the vulnerability once it's fixed

### Security Best Practices

When using QuteWindow, follow these security best practices:

- Keep your dependencies up to date
- Use the latest stable version of QuteWindow
- Review the code before using in security-sensitive applications
- Report any suspicious behavior immediately

## Dependency Security

We regularly scan our dependencies for known vulnerabilities using:

- **safety**: Checks for known security vulnerabilities in dependencies
- **bandit**: Security linter for Python code
- **GitHub Dependabot**: Automated dependency updates

## Security Features

QuteWindow includes several security features:

- **Input Validation**: All user inputs are validated
- **Safe Defaults**: Secure configuration by default
- **No Arbitrary Code Execution**: Prevents code injection attacks
- **Platform Isolation**: Platform-specific code is properly isolated

## Contact

For security-related questions or concerns:
- **Email**: parhamoyan@yahoo.com
- **Subject**: Security Question - QuteWindow

Thank you for helping keep QuteWindow secure!
