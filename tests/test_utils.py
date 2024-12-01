import unittest
from webrover.utils import (
    clean_text, 
    extract_content, 
    validate_url, 
    create_dataset_entry,
    extract_domain,
    chunk_text
)
from bs4 import BeautifulSoup

class TestUtils(unittest.TestCase):
    def test_clean_text(self):
        """Test text cleaning functionality"""
        # Test whitespace handling
        self.assertEqual(clean_text("  hello   world  "), "hello world")
        
        # Test special character removal
        self.assertEqual(clean_text("hello@#$%world!"), "helloworld!")
        
        # Test newlines and tabs
        self.assertEqual(clean_text("hello\n\tworld"), "hello world")

    def test_extract_content(self):
        """Test HTML content extraction"""
        html = """
        <html>
            <head><title>Test Page</title></head>
            <body>
                <h1>Main Heading</h1>
                <p>First paragraph</p>
                <p>Second paragraph</p>
                <div>Some div content</div>
            </body>
        </html>
        """
        content = extract_content(html)
        
        self.assertIn('title', content)
        self.assertIn('content', content)
        self.assertEqual(content['title'], "Test Page")
        self.assertIn("Main Heading", content['content'])
        self.assertIn("First paragraph", content['content'])
        self.assertIn("Second paragraph", content['content'])

    def test_validate_url(self):
        """Test URL validation"""
        # Valid URLs
        self.assertTrue(validate_url("https://example.com"))
        self.assertTrue(validate_url("http://sub.example.com/path"))
        self.assertTrue(validate_url("https://example.com:8080/path?query=1"))
        
        # Invalid URLs
        self.assertFalse(validate_url("not_a_url"))
        self.assertFalse(validate_url("ftp://example.com"))
        self.assertFalse(validate_url("http:/example.com"))

    def test_create_dataset_entry(self):
        """Test dataset entry creation"""
        url = "https://example.com/article"
        title = "Test Article"
        content = "Test content"
        
        entry = create_dataset_entry(url, title, content)
        
        self.assertEqual(entry['url'], url)
        self.assertEqual(entry['title'], title)
        self.assertEqual(entry['content'], content)
        self.assertIn('metadata', entry)
        self.assertIn('length', entry['metadata'])
        self.assertIn('has_title', entry['metadata'])
        self.assertIn('domain', entry['metadata'])
        
        # Test metadata values
        self.assertEqual(entry['metadata']['length'], len(content))
        self.assertTrue(entry['metadata']['has_title'])
        self.assertEqual(entry['metadata']['domain'], 'example.com')

    def test_extract_domain(self):
        """Test domain extraction from URLs"""
        # Standard URLs
        self.assertEqual(extract_domain("https://example.com"), "example.com")
        self.assertEqual(extract_domain("http://sub.example.com"), "sub.example.com")
        self.assertEqual(extract_domain("https://example.com/path"), "example.com")
        
        # URLs with www
        self.assertEqual(extract_domain("https://www.example.com"), "example.com")
        
        # Invalid URLs
        self.assertEqual(extract_domain("not_a_url"), "")

    def test_chunk_text(self):
        """Test text chunking functionality"""
        text = "This is a test sentence. " * 10
        chunk_size = 50
        
        chunks = chunk_text(text, chunk_size)
        
        # Test that chunks are created
        self.assertGreater(len(chunks), 1)
        
        # Test that chunks are roughly the right size
        for chunk in chunks:
            self.assertLessEqual(len(chunk), chunk_size + 20)  # Allow some flexibility
            
        # Test that no content is lost
        combined = " ".join(chunks)
        self.assertEqual(len(combined.split()), len(text.split()))

    def test_extract_content_with_empty_html(self):
        """Test content extraction with empty or invalid HTML"""
        content = extract_content("")
        self.assertEqual(content['title'], "")
        self.assertEqual(content['content'], "")
        
        content = extract_content("<html></html>")
        self.assertEqual(content['title'], "")
        self.assertEqual(content['content'], "")

    def test_create_dataset_entry_empty_inputs(self):
        """Test dataset entry creation with empty inputs"""
        entry = create_dataset_entry("", "", "")
        
        self.assertEqual(entry['url'], "")
        self.assertEqual(entry['title'], "")
        self.assertEqual(entry['content'], "")
        self.assertEqual(entry['metadata']['length'], 0)
        self.assertFalse(entry['metadata']['has_title'])
        self.assertEqual(entry['metadata']['domain'], "")

    def test_extract_content_complex_html(self):
        """Test content extraction from complex HTML"""
        html = """
        <html>
            <head>
                <title>Complex Page</title>
                <meta charset="utf-8">
            </head>
            <body>
                <article>
                    <h1>Main Article</h1>
                    <div class="content">
                        <p>First paragraph with <b>bold</b> text</p>
                        <p>Second paragraph with <i>italic</i> text</p>
                    </div>
                    <div class="comments">
                        <p>Comment 1</p>
                        <p>Comment 2</p>
                    </div>
                </article>
            </body>
        </html>
        """
        content = extract_content(html)
        self.assertIn("Main Article", content['content'])
        self.assertIn("bold", content['content'])
        self.assertIn("italic", content['content'])

    def test_clean_text_special_cases(self):
        """Test text cleaning with special cases"""
        # Test Unicode characters
        self.assertEqual(clean_text("Hello™ World®"), "Hello World")
        
        # Test multiple spaces and punctuation
        self.assertEqual(clean_text("Hello,  World!  How.are.you?"), "Hello, World! How.are.you?")
        
        # Test numbers and special characters
        self.assertEqual(clean_text("Price: $100.00"), "Price 100.00")

    def test_validate_url_edge_cases(self):
        """Test URL validation edge cases"""
        # Test URLs with fragments
        self.assertTrue(validate_url("https://example.com/page#section"))
        
        # Test URLs with query parameters
        self.assertTrue(validate_url("https://example.com/search?q=test&page=1"))
        
        # Test URLs with special characters
        self.assertTrue(validate_url("https://example.com/path%20with%20spaces")) 