import unittest
from webrover import WebRover
import asyncio
import os
import json
import aiohttp
import pytest

class TestWebRover(unittest.TestCase):
    def setUp(self):
        self.rover = WebRover(output_dir="test_dataset")
        
    def tearDown(self):
        # Clean up test files
        if os.path.exists("test_dataset"):
            for file in os.listdir("test_dataset"):
                os.remove(os.path.join("test_dataset", file))
            os.rmdir("test_dataset")

    def test_initialization(self):
        """Test WebRover initialization"""
        self.assertTrue(os.path.exists("test_dataset"))
        self.assertEqual(self.rover.dataset, [])
        self.assertEqual(self.rover.master_urls, {})
        self.assertEqual(self.rover.completed_urls, {})
        self.assertEqual(self.rover.error_urls, {})

    def test_validate_topics_list(self):
        """Test topic validation with list input"""
        topics = ["AI basics", "machine learning"]
        self.rover.scrape_topics(topics=topics, sites_per_topic=1)
        self.assertGreater(len(self.rover.master_urls), 0)

    def test_save_dataset(self):
        """Test dataset saving functionality"""
        test_data = {
            "url": "https://test.com",
            "title": "Test Title",
            "content": "Test Content",
            "metadata": {"length": 12, "has_title": True, "domain": "test.com"}
        }
        self.rover.dataset = [test_data]
        self.rover.save_dataset("test.jsonl")
        
        # Verify file exists and content is correct
        self.assertTrue(os.path.exists(os.path.join("test_dataset", "test.jsonl")))
        with open(os.path.join("test_dataset", "test.jsonl"), 'r') as f:
            saved_data = json.loads(f.read().strip())
            self.assertEqual(saved_data, test_data)

    def test_get_stats(self):
        """Test statistics calculation"""
        self.rover.master_urls = {"url1": "topic1", "url2": "topic2"}
        self.rover.completed_urls = {"url1": {}}
        self.rover.error_urls = {"url2": "error"}
        
        stats = self.rover.get_stats()
        self.assertEqual(stats["total_urls"], 2)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["errors"], 1)
        self.assertEqual(stats["success_rate"], 0.5)

    def test_load_topics_from_file(self):
        """Test loading topics from different file formats"""
        # Test JSON format
        with open("test_topics.json", "w") as f:
            json.dump({"topics": ["AI", "ML"]}, f)
        self.rover.scrape_topics("test_topics.json", sites_per_topic=1)
        os.remove("test_topics.json")
        
        # Test YAML format
        with open("test_topics.yaml", "w") as f:
            f.write("topics:\n  - AI\n  - ML")
        self.rover.scrape_topics("test_topics.yaml", sites_per_topic=1)
        os.remove("test_topics.yaml")
        
        # Test Markdown format
        with open("test_topics.md", "w") as f:
            f.write("- AI\n- ML")
        self.rover.scrape_topics("test_topics.md", sites_per_topic=1)
        os.remove("test_topics.md")

    @pytest.mark.asyncio
    async def test_error_handling(self):
        """Test error handling in scraping process"""
        async with aiohttp.ClientSession() as session:
            await self.rover._scrape_website("invalid_url", session)
            self.assertIn("invalid_url", self.rover.error_urls)
        
        # Test invalid file format
        with self.assertRaises(ValueError):
            self.rover.scrape_topics("test.txt", sites_per_topic=1)

    def test_empty_topics(self):
        """Test handling of empty topics"""
        with self.assertRaises(ValueError):
            self.rover.scrape_topics([], sites_per_topic=1) 