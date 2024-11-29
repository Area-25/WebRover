# Changelog

All notable changes to WebRover will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.11] - 2024-11-29

### Changed
- Renamed `num_websites` parameter to `sites_per_topic` for clarity
- Changed scraping behavior to handle sites per topic instead of total sites
- Updated documentation and examples to reflect new parameter
- Improved parameter descriptions in docstrings

### Fixed
- Clarified confusion about number of websites to scrape per topic
- Updated example code to demonstrate correct usage
- Fixed potential confusion in progress reporting

## [0.1.10] - 2024-11-29

### Fixed
- Major bug fix: Removed infinite loop in URL collection
- Fixed program hanging/freezing after scraping completion
- Fixed progress bar counting issues
- Resolved circular logic in URL processing
- Fixed timestamp formatting in logs

### Changed
- Simplified URL collection and processing logic
- Improved error handling and logging clarity
- Better progress tracking and status messages
- Cleaner completion process

### Removed
- Removed problematic URL replacement logic (will be reimplemented in future version)

### Note
- The feature to ensure exact number of requested websites (replacing failed scrapes) 
  will be implemented in a future update with a more robust approach

## [0.1.9] - 2024-11-29

### Added
- Comprehensive troubleshooting section in README
- Cloud environment compatibility notes
- Common issues and solutions documentation
- Detailed error resolution guides

### Changed
- Improved documentation structure
- Enhanced README clarity and organization

## [0.1.8] - 2024-11-29

### Added
- Persistent scraping until target number of websites is reached
- Auto-retry mechanism for failed scrapes
- Additional URL collection when needed
- Maximum attempts limit to prevent infinite loops
- Enhanced progress tracking for successful scrapes

### Changed
- Improved scraping logic to ensure complete datasets
- Better handling of failed scraping attempts
- More detailed progress reporting

## [0.1.7] - 2024-11-29

### Added
- CHANGELOG.md to track version history
- MANIFEST.in for proper package file inclusion
- Better package metadata handling

### Changed
- Updated setup.py to include CHANGELOG.md and LICENSE
- Improved package distribution structure

## [0.1.6] - 2024-11-29

### Added
- Progress bar with tqdm integration
- Display of dataset save location after completion
- Final statistics summary display

### Changed
- Updated dependencies to include tqdm
- Enhanced progress tracking format

## [0.1.5] - 2024-11-29

### Added
- Enhanced logging with emojis for better visibility
- Detailed status messages for each operation
- Clear success/error indicators

### Changed
- Improved log message formatting
- More descriptive process status updates

## [0.1.4] - 2024-11-29

### Added
- Display of current website being scraped
- Loading status indicators during scraping
- Better error reporting

### Changed
- Improved console output readability
- Enhanced error message clarity

## [0.1.3] - 2024-11-29

### Added
- Detailed logging for each scraping step
- Process start/end notifications
- Status updates for URL collection

### Fixed
- Character encoding issues in logging
- Console output formatting

## [0.1.2] - 2024-11-29

### Added
- Basic logging functionality
- Support for multiple input formats (JSON, YAML, TXT, MD)
- Async web scraping capabilities
- Rate limiting for Google searches
- Error handling and statistics

### Fixed
- Encoding issues in setup.py
- Package installation dependencies

## [0.1.1] - 2024-11-28

### Added
- Initial release
- Basic web scraping functionality
- Google search integration
- Dataset generation in JSONL format
- Basic example scripts 