import re
from typing import Dict, List, Optional
from pathlib import Path
import json
from bs4 import BeautifulSoup
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """Clean and normalize text content."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()

def extract_content(html: str, selectors: Optional[List[str]] = None) -> Dict[str, str]:
    """Extract content from HTML using BeautifulSoup."""
    if selectors is None:
        selectors = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract title
    title = soup.title.string if soup.title else ''
    
    # Extract main content
    content = ' '.join([
        p.get_text() 
        for p in soup.find_all(selectors)
    ])
    
    return {
        'title': clean_text(title),
        'content': clean_text(content)
    }

def save_json(data: Dict, filepath: Path, indent: int = 2) -> None:
    """Safely save JSON data to file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error saving JSON to {filepath}: {str(e)}")
        raise

def load_json(filepath: Path) -> Dict:
    """Safely load JSON data from file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        logger.error(f"Error loading JSON from {filepath}: {str(e)}")
        raise

def validate_url(url: str) -> bool:
    """Validate URL format."""
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None

def create_dataset_entry(url: str, title: str, content: str) -> Dict:
    """Create a standardized dataset entry."""
    return {
        'url': url,
        'title': title,
        'content': content,
        'metadata': {
            'length': len(content),
            'has_title': bool(title),
            'domain': extract_domain(url)
        }
    }

def extract_domain(url: str) -> str:
    """Extract domain from URL."""
    match = re.search(r'https?://(?:www\.)?([^/]+)', url)
    return match.group(1) if match else ''

def chunk_text(text: str, chunk_size: int = 1000) -> List[str]:
    """Split text into chunks of approximately equal size."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        word_size = len(word)
        if current_size + word_size > chunk_size and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]
            current_size = word_size
        else:
            current_chunk.append(word)
            current_size += word_size
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks
