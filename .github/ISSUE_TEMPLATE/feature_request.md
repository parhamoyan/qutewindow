---
name: Feature Request
description: Suggest a new feature for QuteWindow
title: "[FEATURE] "
labels: ["enhancement", "needs-triage"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting a new feature! Please provide as much detail as possible to help us understand your request.

  - type: textarea
    id: feature-description
    attributes:
      label: Feature Description
      description: A clear and concise description of the feature you'd like to see
      placeholder: Describe the feature you'd like to see implemented...
    validations:
      required: true

  - type: textarea
    id: problem-statement
    attributes:
      label: Problem Statement
      description: Is your feature request related to a problem? If so, please describe it
      placeholder: I'm frustrated when... It would be helpful if...
    validations:
      required: true

  - type: textarea
    id: proposed-solution
    attributes:
      label: Proposed Solution
      description: Describe the solution you'd like to see implemented
      placeholder: I would like QuteWindow to...
    validations:
      required: true

  - type: textarea
    id: use-cases
    attributes:
      label: Use Cases
      description: Describe specific use cases where this feature would be beneficial
      placeholder: |
        1. When building a media player application...
        2. For creating custom dialog boxes...
        3. In enterprise applications that require...
    validations:
      required: true

  - type: textarea
    id: alternatives-considered
    attributes:
      label: Alternatives Considered
      description: Describe any alternative solutions or features you've considered
      placeholder: I've considered using... but it doesn't work because...
    validations:
      required: false

  - type: dropdown
    id: priority
    attributes:
      label: Priority
      description: How important is this feature to you?
      options:
        - Low (nice to have)
        - Medium (would improve my workflow)
        - High (blocking my current work)
        - Critical (preventing me from using QuteWindow)
    validations:
      required: true

  - type: textarea
    id: implementation-suggestions
    attributes:
      label: Implementation Suggestions
      description: Do you have any suggestions for how this could be implemented?
      placeholder: This could be implemented by adding a new method to the QuteWindow class...
    validations:
      required: false

  - type: textarea
    id: additional-context
    attributes:
      label: Additional Context
      description: Add any other context, screenshots, or examples about the feature request
      placeholder: Any additional information that might be helpful...

  - type: checkboxes
    id: terms
    attributes:
      label: Checklist
      description: Please confirm the following
      options:
        - label: I have searched existing issues to ensure this is not a duplicate
          required: true
        - label: I have provided a clear description of the feature
          required: true
        - label: I am willing to help implement this feature (optional)
          required: false
