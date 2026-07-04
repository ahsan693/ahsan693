#!/usr/bin/env python3
"""
Demonstration script for Min and Max Heap implementations.
Uses the frequency data provided in the problem statement.
"""

from heaps import Node, MinHeap, MaxHeap


def test_max_heap():
    """Test MaxHeap with provided frequency data."""
    print("=== Testing MaxHeap ===")
    
    # MaxHeap frequencies from problem statement
    max_heap_data = [
        ('p', 63), ('q', 36), ('r', 73), ('t', 57),
        ('a', 85), ('b', 52), ('g', 69), ('h', 44)
    ]
    
    max_heap = MaxHeap()
    
    # Insert all nodes
    print("Inserting nodes into MaxHeap:")
    for letter, freq in max_heap_data:
        node = Node(letter, freq)
        max_heap.insert(node)
        print(f"Inserted {node}, heap: {max_heap}")
    
    print(f"\nFinal MaxHeap: {max_heap}")
    print(f"Heap size: {max_heap.size()}")
    print(f"Peek (max element): {max_heap.peek()}")
    
    # Extract elements to verify heap property
    print("\nExtracting elements from MaxHeap (should be in descending order):")
    extracted = []
    while not max_heap.is_empty():
        node = max_heap.extract()
        extracted.append(node)
        print(f"Extracted: {node}, remaining heap: {max_heap}")
    
    print(f"Extracted sequence: {[str(node) for node in extracted]}")
    
    # Verify the sequence is in descending order
    frequencies = [node.frequency for node in extracted]
    is_sorted = all(frequencies[i] >= frequencies[i+1] for i in range(len(frequencies)-1))
    print(f"Is extracted sequence in descending order? {is_sorted}")
    
    return extracted


def test_min_heap():
    """Test MinHeap with provided frequency data."""
    print("\n=== Testing MinHeap ===")
    
    # MinHeap frequencies from problem statement
    min_heap_data = [
        ('p', 22), ('q', 67), ('r', 14), ('t', 31), ('a', 11),
        ('b', 43), ('g', 2), ('h', 52), ('i', 26)
    ]
    
    min_heap = MinHeap()
    
    # Insert all nodes
    print("Inserting nodes into MinHeap:")
    for letter, freq in min_heap_data:
        node = Node(letter, freq)
        min_heap.insert(node)
        print(f"Inserted {node}, heap: {min_heap}")
    
    print(f"\nFinal MinHeap: {min_heap}")
    print(f"Heap size: {min_heap.size()}")
    print(f"Peek (min element): {min_heap.peek()}")
    
    # Extract elements to verify heap property
    print("\nExtracting elements from MinHeap (should be in ascending order):")
    extracted = []
    while not min_heap.is_empty():
        node = min_heap.extract()
        extracted.append(node)
        print(f"Extracted: {node}, remaining heap: {min_heap}")
    
    print(f"Extracted sequence: {[str(node) for node in extracted]}")
    
    # Verify the sequence is in ascending order
    frequencies = [node.frequency for node in extracted]
    is_sorted = all(frequencies[i] <= frequencies[i+1] for i in range(len(frequencies)-1))
    print(f"Is extracted sequence in ascending order? {is_sorted}")
    
    return extracted


def test_heap_operations():
    """Test specific heap operations."""
    print("\n=== Testing Individual Operations ===")
    
    # Test with a small example
    heap = MinHeap()
    
    print("Testing insert and peek operations:")
    nodes = [Node('x', 10), Node('y', 5), Node('z', 15)]
    
    for node in nodes:
        heap.insert(node)
        print(f"After inserting {node}: peek = {heap.peek()}, heap = {heap}")
    
    print("\nTesting extract operations:")
    while not heap.is_empty():
        extracted = heap.extract()
        peek_result = heap.peek() if not heap.is_empty() else "None (empty)"
        print(f"Extracted: {extracted}, new peek = {peek_result}, heap = {heap}")


if __name__ == "__main__":
    print("Min and Max Heap Implementation Demo")
    print("="*50)
    
    # Test MaxHeap
    max_extracted = test_max_heap()
    
    # Test MinHeap  
    min_extracted = test_min_heap()
    
    # Test individual operations
    test_heap_operations()
    
    print("\n" + "="*50)
    print("Demo completed successfully!")
    print(f"MaxHeap extracted {len(max_extracted)} elements in descending order")
    print(f"MinHeap extracted {len(min_extracted)} elements in ascending order")