import os
import pytest
from datetime import datetime
from utils.pdf_parser import parse_pdf  # Import function from util


# Absolute path based on this file's location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # go up 1 level from tests
SAMPLE_PDF = os.path.join(BASE_DIR, "data", "samples", "sample.pdf")


def test_parse_pdf_returns_text_and_metadata():
    text, metadata = parse_pdf(SAMPLE_PDF)
    
    # --- Basic type checks ---
    assert isinstance(text, str), "Text should be a string"
    assert isinstance(metadata, dict), "Metadata should be a dictionary"
    
    # --- Metadata checks ---
    assert "file_name" in metadata
    assert "file_size" in metadata
    assert "date_parsed" in metadata
    
    # --- Logical checks ---
    assert metadata["file_name"].endswith(".pdf"), "File name should end with .pdf"
    assert metadata["file_size"] > 0, "File size should be positive"
    
    # Check ISO format for date
    datetime.fromisoformat(metadata["date_parsed"])
    
    # --- Text content check ---
    assert len(text) > 0, "Extracted text should not be empty"

def test_parse_pdf_invalid_file():
    with pytest.raises(FileNotFoundError):
        parse_pdf("./data/uploads/does_not_exist.pdf")