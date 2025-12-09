#!/usr/bin/env python3
"""
Test the search endpoint
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_search_endpoint():
    """Test the search functionality"""
    
    print("🔍 Testing Search Endpoints")
    print("="*50)
    
    # Test 1: Search by title
    print("\n1. Searching books with 'Great' in title:")
    response = requests.get(f"{BASE_URL}/books/search/?title=Great")
    if response.status_code == 200:
        books = response.json()
        print(f"   Found {len(books)} books:")
        for book in books:
            print(f"   - {book['title']} by {book['author']}")
    else:
        print(f"   Error: {response.status_code}")
    
    # Test 2: Search by author
    print("\n2. Searching books by 'Orwell':")
    response = requests.get(f"{BASE_URL}/books/search/?author=Orwell")
    if response.status_code == 200:
        books = response.json()
        print(f"   Found {len(books)} books:")
        for book in books:
            print(f"   - {book['title']} by {book['author']} ({book['year']})")
    else:
        print(f"   Error: {response.status_code}")
    
    # Test 3: Search by year
    print("\n3. Searching books published in 1949:")
    response = requests.get(f"{BASE_URL}/books/search/?year=1949")
    if response.status_code == 200:
        books = response.json()
        print(f"   Found {len(books)} books:")
        for book in books:
            print(f"   - {book['title']} by {book['author']}")
    else:
        print(f"   Error: {response.status_code}")
    
    # Test 4: Combined search
    print("\n4. Combined search (title='The' and year > 1900):")
    response = requests.get(f"{BASE_URL}/books/?title=The&year=1954")
    if response.status_code == 200:
        books = response.json()
        print(f"   Found {len(books)} books:")
        for book in books:
            print(f"   - {book['title']} by {book['author']} ({book['year']})")
    else:
        print(f"   Error: {response.status_code}")
    
    print("\n" + "="*50)
    print("✅ Search endpoint tests completed!")

if __name__ == "__main__":
    # First, make sure the server is running
    print("Note: Make sure the FastAPI server is running (uvicorn main:app --reload)")
    input("Press Enter to continue testing...")
    test_search_endpoint()