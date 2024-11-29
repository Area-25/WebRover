from setuptools import setup, find_packages
import io

# Read README with proper encoding
with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="webrover",
    version="0.1.11",
    packages=find_packages(),
    install_requires=[
        "aiohttp==3.11.8",
        "beautifulsoup4==4.12.3",
        "googlesearch-python==1.2.5",
        "pyyaml==6.0.2",
        "setuptools==75.6.0",
        "tqdm==4.67.1",
    ],
    author="Area-25",
    author_email="jasonquist.ssh@gmail.com",
    description="Generate high-quality datasets from web content for AI training",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Area-25/webrover",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.10",
    keywords="web-scraping, dataset-generation, machine-learning, ai-training, deep-learning",
    data_files=[
        ('', ['README.md', 'CHANGELOG.md']),
    ],
) 