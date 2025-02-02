# services/data-processor/tests/test_processor.py
from data_processor.processor import process

def test_process():
    assert process(["apple", "banana"]) == ["APPLE", "BANANA"]
