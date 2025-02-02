def process(data):
    """Simple data processor."""
    return [item.upper() for item in data]

if __name__ == "__main__":
    sample_data = ["apple", "banana", "cherry"]
    print(process(sample_data))
