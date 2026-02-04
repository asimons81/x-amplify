"""
Output Validator
Scans generated content for forbidden patterns and AI-isms.
"""

import re
from typing import NamedTuple


class ValidationResult(NamedTuple):
    """Result of content validation."""
    is_valid: bool
    issues: list[str]
    cleaned_content: str | None


# Forbidden patterns
FORBIDDEN_PATTERNS = [
    (r'—', 'Em dash detected'),
    (r'\bdelve\b', 'AI phrase "delve" detected'),
    (r'\bgame-?changer\b', 'AI phrase "game-changer" detected'),
    (r"[Ii]n today'?s world", 'AI phrase "In today\'s world" detected'),
    (r"[Hh]ere'?s the thing", 'AI phrase "Here\'s the thing" detected'),
    (r'\bleveraging\b', 'AI phrase "leveraging" detected'),
    (r'\bunlock\b', 'AI phrase "unlock" detected'),
    (r'\btransformative\b', 'AI phrase "transformative" detected'),
]


def validate_post(content: str) -> ValidationResult:
    """
    Validate a single post for forbidden patterns.
    
    Args:
        content: The post content to validate
        
    Returns:
        ValidationResult with validity status, issues list, and cleaned content
    """
    issues = []
    cleaned = content
    
    for pattern, message in FORBIDDEN_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(message)
            
            # Auto-fix em dashes
            if pattern == r'—':
                cleaned = cleaned.replace('—', '.')
    
    # Check for walls of text (no line breaks in long content)
    if len(content) > 200 and '\n' not in content:
        issues.append('Wall of text detected (missing line breaks)')
    
    return ValidationResult(
        is_valid=len(issues) == 0,
        issues=issues,
        cleaned_content=cleaned if cleaned != content else None
    )


def validate_all_posts(posts: dict[str, str]) -> dict[str, ValidationResult]:
    """
    Validate all posts in the response.
    
    Args:
        posts: Dictionary of format_name -> post_content
        
    Returns:
        Dictionary of format_name -> ValidationResult
    """
    return {name: validate_post(content) for name, content in posts.items()}


def has_critical_issues(validation_results: dict[str, ValidationResult]) -> bool:
    """Check if any posts have critical issues that require re-generation."""
    for result in validation_results.values():
        for issue in result.issues:
            if 'Em dash' in issue:
                return True
    return False
