from data_processor.processor import process
from text.converter import extract_names_from_text

def extract_and_process_names(names):
    """
    Takes a list of names, processes them using data-processor,
    and returns the processed names.
    """
    processed_names = process(names)
    return processed_names

if __name__ == "__main__":
    #sample_names = ["alice", "bob", "charlie"]
    sample_names = extract_names_from_text(" Alice and Leo")
    result = extract_and_process_names(sample_names)
    print("Processed Names:", result)
