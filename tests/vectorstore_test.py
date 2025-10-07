import pytest
from utils.vectorstore import add_to_chroma, query_chroma

def test_add_and_query_chroma():
    doc_id = "test_doc"
    text = "This is a sample text to test the Chroma embeddings and query pipeline."
    
    # Add document
    add_to_chroma(doc_id, text)
    
    # Query for something similar
    query = "sample text"
    results = query_chroma(query, top_k=1)
    
    # Basic checks
    assert "documents" in results
    assert len(results['documents']) > 0
    assert text[:50] in results['documents'][0][0]  # first chunk matches

def test_query_empty():
    # Query something that doesn't exist
    query = "completely unrelated text"
    results = query_chroma(query, top_k=1)
    
    # Should still return something, but maybe irrelevant
    assert "documents" in results