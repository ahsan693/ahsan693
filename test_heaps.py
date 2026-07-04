#!/usr/bin/env python3
"""
Unit tests for Min and Max Heap implementations.
"""

from heaps import Node, MinHeap, MaxHeap


def test_node_creation():
    """Test Node class creation and string representation."""
    node = Node('a', 10)
    assert node.letter == 'a'
    assert node.frequency == 10
    assert str(node) == 'a:10'
    print("✓ Node creation test passed")


def test_min_heap_property():
    """Test that MinHeap maintains min heap property."""
    heap = MinHeap()
    
    # Insert test data
    test_data = [('a', 10), ('b', 5), ('c', 15), ('d', 3), ('e', 8)]
    for letter, freq in test_data:
        heap.insert(Node(letter, freq))
    
    # Verify heap property: each parent should be <= children
    def verify_min_heap_property(heap_array):
        for i in range(len(heap_array)):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if left_child < len(heap_array):
                if heap_array[i].frequency > heap_array[left_child].frequency:
                    return False
            
            if right_child < len(heap_array):
                if heap_array[i].frequency > heap_array[right_child].frequency:
                    return False
        return True
    
    assert verify_min_heap_property(heap.heap), "Min heap property violated"
    assert heap.peek().frequency == 3, "Minimum element should be at root"
    print("✓ MinHeap property test passed")


def test_max_heap_property():
    """Test that MaxHeap maintains max heap property."""
    heap = MaxHeap()
    
    # Insert test data
    test_data = [('a', 10), ('b', 5), ('c', 15), ('d', 3), ('e', 8)]
    for letter, freq in test_data:
        heap.insert(Node(letter, freq))
    
    # Verify heap property: each parent should be >= children
    def verify_max_heap_property(heap_array):
        for i in range(len(heap_array)):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            if left_child < len(heap_array):
                if heap_array[i].frequency < heap_array[left_child].frequency:
                    return False
            
            if right_child < len(heap_array):
                if heap_array[i].frequency < heap_array[right_child].frequency:
                    return False
        return True
    
    assert verify_max_heap_property(heap.heap), "Max heap property violated"
    assert heap.peek().frequency == 15, "Maximum element should be at root"
    print("✓ MaxHeap property test passed")


def test_extract_order():
    """Test that extract operations return elements in correct order."""
    # Test MinHeap
    min_heap = MinHeap()
    frequencies = [30, 10, 40, 5, 15]
    for i, freq in enumerate(frequencies):
        min_heap.insert(Node(chr(ord('a') + i), freq))
    
    extracted_min = []
    while not min_heap.is_empty():
        extracted_min.append(min_heap.extract().frequency)
    
    assert extracted_min == sorted(frequencies), "MinHeap extract order incorrect"
    print("✓ MinHeap extract order test passed")
    
    # Test MaxHeap
    max_heap = MaxHeap()
    for i, freq in enumerate(frequencies):
        max_heap.insert(Node(chr(ord('a') + i), freq))
    
    extracted_max = []
    while not max_heap.is_empty():
        extracted_max.append(max_heap.extract().frequency)
    
    assert extracted_max == sorted(frequencies, reverse=True), "MaxHeap extract order incorrect"
    print("✓ MaxHeap extract order test passed")


def test_empty_heap_operations():
    """Test operations on empty heaps."""
    min_heap = MinHeap()
    max_heap = MaxHeap()
    
    # Test empty heap properties
    assert min_heap.is_empty() == True
    assert max_heap.is_empty() == True
    assert min_heap.size() == 0
    assert max_heap.size() == 0
    assert min_heap.peek() is None
    assert max_heap.peek() is None
    assert min_heap.extract() is None
    assert max_heap.extract() is None
    
    print("✓ Empty heap operations test passed")


def test_single_element():
    """Test heap operations with single element."""
    min_heap = MinHeap()
    max_heap = MaxHeap()
    
    node = Node('x', 42)
    
    # Test single element operations
    min_heap.insert(node)
    max_heap.insert(node)
    
    assert min_heap.size() == 1
    assert max_heap.size() == 1
    assert min_heap.peek().frequency == 42
    assert max_heap.peek().frequency == 42
    
    # Extract the element
    extracted_min = min_heap.extract()
    extracted_max = max_heap.extract()
    
    assert extracted_min.frequency == 42
    assert extracted_max.frequency == 42
    assert min_heap.is_empty()
    assert max_heap.is_empty()
    
    print("✓ Single element test passed")


def run_all_tests():
    """Run all tests."""
    print("Running heap implementation tests...")
    print("-" * 40)
    
    test_node_creation()
    test_min_heap_property()
    test_max_heap_property()
    test_extract_order()
    test_empty_heap_operations()
    test_single_element()
    
    print("-" * 40)
    print("✓ All tests passed successfully!")


if __name__ == "__main__":
    run_all_tests()