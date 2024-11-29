from webrover import WebRover

# Initialize WebRover
rover = WebRover()

# Test with a simple topic
rover.scrape_topics(
    topics=["artificial intelligence basics"],
    num_websites=10
)

rover.save_dataset("file_topics.jsonl")

# Print stats
stats = rover.get_stats()
print("\nScraping Results:")
print(f"Success rate: {stats['success_rate']*100:.1f}%")
print(f"Total URLs: {stats['total_urls']}")
print(f"Completed: {stats['completed']}")
print(f"Errors: {stats['errors']}")