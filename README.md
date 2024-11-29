# WebRover 🚀

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**WebRover is a powerful Python library for generating high-quality datasets from web content, designed specifically for training Large Language Models and AI applications.**

---

## 🌟 Features

- **Smart Web Scraping**: Automatically find and scrape relevant content based on topics
- **Multiple Input Formats**: Support for JSON, YAML, TXT, and Markdown topic files
- **Async Processing**: Fast, concurrent scraping with built-in rate limiting
- **Quality Control**: Built-in content validation and cleaning
- **LLM-Ready Output**: Structured JSONL format perfect for model training
- **Error Handling**: Robust error tracking and recovery mechanisms

## ⚠️ Important Notes

### Cloud Environment Compatibility

When using WebRover in cloud environments like Google Colab or Kaggle Notebooks, you may need to handle nested asyncio loops. This is a limitation of these environments, not WebRover itself. To resolve this:

1. Install nest_asyncio:
```bash
pip install nest_asyncio
```

2. Add these lines at the start of your notebook:
```python
import nest_asyncio
nest_asyncio.apply()
```

This setup is only required for:
- Google Colab
- Kaggle Notebooks
- Similar cloud-based Jupyter environments

It's not needed for:
- Local Python scripts
- Command line usage
- Standard server deployments

## 🚀 Troubleshooting

### Cloud Environment Issues

When using WebRover in cloud environments (Google Colab, Kaggle Notebooks), you may encounter asyncio-related errors. This is due to how these environments handle async operations. To fix:

```python
# Install the required package
pip install nest_asyncio

# Add at the start of your notebook
import nest_asyncio
nest_asyncio.apply()
```

### Common Issues and Solutions

1. **Rate Limiting**
   - Symptom: Many HTTP 429 errors
   - Solution: Decrease scraping speed by increasing sleep time between requests

2. **Memory Issues with Large Datasets**
   - Symptom: Out of memory errors
   - Solution: Use smaller batch sizes or enable disk caching

3. **Blocked Access**
   - Symptom: HTTP 403 Forbidden errors
   - Solution: Ensure your user agent is set correctly and respect robots.txt

4. **SSL Certificate Errors**
   - Symptom: SSL verification failed
   - Solution: Update your Python SSL certificates or check network settings

## 🚀 Quick Start

### Installation
```bash
pip install webrover
```

### Basic Usage
```python
from webrover import WebRover

# Initialize WebRover
rover = WebRover()

# Scrape content from topics
rover.scrape_topics(
    topics=["artificial intelligence", "machine learning"],
    sites_per_topic=20  # Will get 20 sites for each topic
)

# Save the dataset
rover.save_dataset("my_dataset.jsonl")
```

### Using Topic Files
```python
# From JSON file
rover.scrape_topics(
    topics="topics.json",
    num_websites=100
)

# From Markdown list
rover.scrape_topics(
    topics="topics.md",
    num_websites=100
)
```

## 📖 Documentation

### Supported Topic File Formats

#### JSON
```json
{
    "topics": [
        "AI basics",
        "machine learning",
        "deep learning"
    ]
}
```

#### YAML
```yaml
topics:
  - AI basics
  - machine learning
  - deep learning
```

#### Markdown
```markdown
- AI basics
- machine learning
- deep learning
```

### Output Structure
```python
{
    'url': 'https://example.com/article',
    'title': 'Article Title',
    'content': 'Article content...',
    'metadata': {
        'length': 1234,
        'has_title': true,
        'domain': 'example.com'
    }
}
```

## 🛠️ Advanced Usage

```python
# Initialize with custom output directory
rover = WebRover(output_dir="my_datasets")

# Get scraping statistics
stats = rover.get_stats()
print(f"Success rate: {stats['success_rate']*100:.1f}%")

# Access dataset programmatically
dataset = rover.get_dataset()
```

## 📊 Output Files

- `final_dataset/dataset.jsonl`: Main dataset in JSONL format
- `websites_master.json`: List of all discovered URLs
- `websites_completed.json`: Successfully scraped URLs
- `websites_errors.json`: Failed attempts with error details

## 🔄 Error Handling

WebRover automatically handles common issues:
- Rate limiting
- Network timeouts
- Invalid URLs
- Blocked requests
- Malformed content

## 🚧 Limitations

- Respects robots.txt and site rate limits
- Some sites may block automated access
- Large datasets require more processing time
- Google search may throttle excessive requests

## 🗺️ Roadmap

See [FUTURE.md](FUTURE.md) for planned features and improvements.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with ❤️ by Area-25. Special thanks to all contributors.

---

**WebRover: Build better datasets, train better models.** 🚀
