from webrover import WebRover
import json

def example_direct_topics():
    """Example using direct topic list"""
    rover = WebRover(output_dir="my_dataset")
    
    # Direct topics list
    rover.scrape_topics(
        topics=["artificial intelligence basics", "machine learning fundamentals"],
        sites_per_topic=10
    )
    rover.save_dataset("direct_topics.jsonl")
    return rover.get_stats()

def example_file_topics():
    """Example using topics from file"""
    # First create a topics file
    topics = {
        "topics": [
            "deep learning architectures",
            "neural networks explained",
            "machine learning algorithms"
        ]
    }
    
    with open("topics.json", "w") as f:
        json.dump(topics, f, indent=2)
    
    # Now use the file
    rover = WebRover(output_dir="my_dataset")
    rover.scrape_topics(
        topics="topics.json",
        sites_per_topic=15
    )
    rover.save_dataset("file_topics.jsonl")
    return rover.get_stats()

if __name__ == "__main__":
    # Try both methods
    print("\n=== Direct Topics Example ===")
    stats1 = example_direct_topics()
    print(f"Success rate: {stats1['success_rate']*100:.2f}%")
    print(f"Total URLs: {stats1['total_urls']}")
    print(f"Completed: {stats1['completed']}")
    print(f"Errors: {stats1['errors']}")
    
    print("\n=== File Topics Example ===")
    stats2 = example_file_topics()
    print(f"Success rate: {stats2['success_rate']*100:.2f}%")
    print(f"Total URLs: {stats2['total_urls']}")
    print(f"Completed: {stats2['completed']}")
    print(f"Errors: {stats2['errors']}") 