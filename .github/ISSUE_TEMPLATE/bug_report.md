---
name: Bug Report
description: Report a bug to help us improve QuteWindow
title: "[BUG] "
labels: ["bug", "needs-triage"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report! Please provide as much detail as possible to help us understand and reproduce the issue.

  - type: textarea
    id: bug-description
    attributes:
      label: Bug Description
      description: A clear and concise description of what the bug is
      placeholder: Describe the bug...
    validations:
      required: true

  - type: textarea
    id: reproduction-steps
    attributes:
      label: Reproduction Steps
      description: Steps to reproduce the behavior
      placeholder: |
        1. Install QuteWindow with 'pip install qutewindow'
        2. Create a new Python file with the following code...
        3. Run the script
        4. See error
    validations:
      required: true

  - type: textarea
    id: expected-behavior
    attributes:
      label: Expected Behavior
      description: A clear and concise description of what you expected to happen
      placeholder: What should have happened?
    validations:
      required: true

  - type: textarea
    id: actual-behavior
    attributes:
      label: Actual Behavior
      description: A clear and concise description of what actually happened
      placeholder: What actually happened?
    validations:
      required: true

  - type: textarea
    id: error-messages
    attributes:
      label: Error Messages
      description: Include any error messages, stack traces, or screenshots
      placeholder: Paste error messages or stack traces here...
      render: shell

  - type: input
    id: qutewindow-version
    attributes:
      label: QuteWindow Version
      description: What version of QuteWindow are you using?
      placeholder: "0.2.0"
    validations:
      required: true

  - type: input
    id: python-version
    attributes:
      label: Python Version
      description: What version of Python are you using?
      placeholder: "3.11.0"
    validations:
      required: true

  - type: dropdown
    id: operating-system
    attributes:
      label: Operating System
      description: What operating system are you using?
      options:
        - Windows 11
        - Windows 10
        - macOS 14+ (Sonoma)
        - macOS 13+ (Ventura)
        - macOS 12+ (Monterey)
        - Linux (Ubuntu)
        - Linux (Other)
        - Other
    validations:
      required: true

  - type: dropdown
    id: qt-binding
    attributes:
      label: Qt Binding
      description: Which Qt binding are you using?
      options:
        - PySide6
        - PyQt6
        - PySide2
        - PyQt5
        - Other
    validations:
      required: true

  - type: textarea
    id: additional-context
    attributes:
      label: Additional Context
      description: Add any other context about the problem here
      placeholder: Any additional information that might be helpful...

  - type: checkboxes
    id: terms
    attributes:
      label: Checklist
      description: Please confirm the following
      options:
        - label: I have searched existing issues to ensure this is not a duplicate
          required: true
        - label: I have provided all the requested information
          required: true
        - label: I am able to reproduce the issue consistently
          required: false
