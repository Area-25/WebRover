from webrover import WebRover

def main():
    # Initialize WebRover
    rover = WebRover()

    # Method 1: Simple list of topics
    rover.scrape_topics(
        topics=["artificial intelligence", "machine learning"],
        sites_per_topic=5  # Start small for testing
    )
    
    # Save the dataset
    rover.save_dataset()
    
    # Print results
    stats = rover.get_stats()
    print(f"\nScraping Results:")
    print(f"✓ Success rate: {stats['success_rate']*100:.1f}%")
    print(f"✓ Total websites: {stats['total_urls']}")
    print(f"✓ Successfully scraped: {stats['completed']}")
    print(f"✗ Failed: {stats['errors']}")

if __name__ == "__main__":
    main() 