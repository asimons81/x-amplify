"""
Gemini Engine
Handles all interactions with Gemini 3 Pro via google-genai SDK.
"""

import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

from config.prompts import (
    THESIS_EXTRACTION_PROMPT,
    STIJN_METHOD_PROMPT,
    POSTS_JSON_SCHEMA,
)
from logic.validator import validate_all_posts, has_critical_issues

# Load environment variables
load_dotenv()
import streamlit as st


class GeminiEngine:
    """Handles Gemini 3 Pro API interactions."""
    
    def __init__(self):
        """Initialize the Gemini client."""
        # Try environment variable first (local), then Streamlit secrets (cloud)
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            try:
                api_key = st.secrets["GEMINI_API_KEY"]
            except Exception:
                pass
                
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables or Streamlit secrets")
        
        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3-flash-preview"
    
    def extract_thesis(self, content: str) -> str:
        """
        Step 1: Extract the Core Value Proposition from input content.
        
        Args:
            content: The raw content (from URL or direct text)
            
        Returns:
            The distilled thesis statement
        """
        prompt = THESIS_EXTRACTION_PROMPT.format(input_content=content)
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=100,
            ),
        )
        
        return response.text.strip()
    
    def generate_all_formats(self, thesis: str, max_retries: int = 2) -> dict[str, str]:
        """
        Step 2: Generate all 10 Stijn formats from the thesis.
        
        Args:
            thesis: The core value proposition
            max_retries: Number of retries if validation fails
            
        Returns:
            Dictionary with all 10 post formats
        """
        prompt = STIJN_METHOD_PROMPT.format(thesis=thesis)
        
        for attempt in range(max_retries + 1):
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.8,
                    max_output_tokens=4000,
                    response_mime_type="application/json",
                    response_schema=POSTS_JSON_SCHEMA,
                ),
            )
            
            try:
                posts = json.loads(response.text)
            except json.JSONDecodeError:
                # If JSON parsing fails, try to extract JSON from response
                import re
                json_match = re.search(r'\{[\s\S]*\}', response.text)
                if json_match:
                    posts = json.loads(json_match.group())
                else:
                    raise ValueError("Failed to parse JSON response from Gemini")
            
            # Validate posts
            validation_results = validate_all_posts(posts)
            
            # Auto-fix em dashes
            for key, result in validation_results.items():
                if result.cleaned_content:
                    posts[key] = result.cleaned_content
            
            # If no critical issues or last attempt, return
            if not has_critical_issues(validation_results) or attempt == max_retries:
                # Convert \n strings to actual newlines for display
                for key in posts:
                    posts[key] = posts[key].replace('\\n', '\n')
                return posts
            
            # Add retry context to prompt
            prompt += "\n\nIMPORTANT: Previous attempt contained em dashes. DO NOT use — anywhere."
        
        return posts
    
    def generate_content(self, user_input: str, input_type: str, content: str) -> tuple[str, dict[str, str]]:
        """
        Full pipeline: Extract thesis and generate all formats.
        
        Args:
            user_input: Original user input (for reference)
            input_type: "url" or "text"
            content: Processed content to analyze
            
        Returns:
            Tuple of (thesis, posts_dict)
        """
        # Step 1: Extract thesis
        thesis = self.extract_thesis(content)
        
        # Step 2: Generate all formats
        posts = self.generate_all_formats(thesis)
        
        return (thesis, posts)
