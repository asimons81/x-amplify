"""
URL Content Scraper
Extracts main text content from web pages using BeautifulSoup4.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re


def is_valid_url(text: str) -> bool:
    """Check if the input string is a valid URL."""
    try:
        result = urlparse(text.strip())
        return all([result.scheme in ('http', 'https'), result.netloc])
    except Exception:
        return False


def extract_content_from_url(url: str) -> str:
    """
    Scrape a URL and extract the main text content.
    
    Args:
        url: The URL to scrape
        
    Returns:
        Extracted text content from the page
        
    Raises:
        Exception: If scraping fails
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url.strip(), headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch URL: {str(e)}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remove script and style elements
    for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
        element.decompose()
    
    # Try to find main content areas
    main_content = None
    
    # Priority: article > main > body
    for selector in ['article', 'main', '[role="main"]', '.post-content', '.article-body']:
        main_content = soup.select_one(selector)
        if main_content:
            break
    
    if not main_content:
        main_content = soup.body if soup.body else soup
    
    # Extract text
    text = main_content.get_text(separator='\n', strip=True)
    
    # Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    
    # Limit content length (for token efficiency)
    max_chars = 8000
    if len(text) > max_chars:
        text = text[:max_chars] + "..."
    
    return text


def smart_input_parser(user_input: str) -> tuple[str, str]:
    """
    Parse user input and determine if it's a URL or raw text.
    
    Args:
        user_input: The raw input from the user
        
    Returns:
        Tuple of (input_type, processed_content)
        input_type is either "url" or "text"
    """
    user_input = user_input.strip()
    
    if is_valid_url(user_input):
        content = extract_content_from_url(user_input)
        return ("url", content)
    else:
        return ("text", user_input)
