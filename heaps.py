class Node:
    """A node class to store letter and frequency for heap operations."""
    
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
    
    def __str__(self):
        return f"{self.letter}:{self.frequency}"
    
    def __repr__(self):
        return f"Node('{self.letter}', {self.frequency})"


class MinHeap:
    """Min Heap implementation where parent nodes have smaller frequencies than children."""
    
    def __init__(self):
        self.heap = []
    
    def _parent_index(self, index):
        """Get parent index for given index."""
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        """Get left child index for given index."""
        return 2 * index + 1
    
    def _right_child_index(self, index):
        """Get right child index for given index."""
        return 2 * index + 2
    
    def _swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, index):
        """Move element up the heap to maintain min heap property."""
        while index > 0:
            parent_idx = self._parent_index(index)
            if self.heap[index].frequency >= self.heap[parent_idx].frequency:
                break
            self._swap(index, parent_idx)
            index = parent_idx
    
    def heapify_down(self, index):
        """Move element down the heap to maintain min heap property."""
        while True:
            smallest = index
            left_idx = self._left_child_index(index)
            right_idx = self._right_child_index(index)
            
            # Check if left child is smaller
            if (left_idx < len(self.heap) and 
                self.heap[left_idx].frequency < self.heap[smallest].frequency):
                smallest = left_idx
            
            # Check if right child is smaller
            if (right_idx < len(self.heap) and 
                self.heap[right_idx].frequency < self.heap[smallest].frequency):
                smallest = right_idx
            
            # If no change needed, break
            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest
    
    def insert(self, node):
        """Insert a new node into the heap."""
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)
    
    def extract(self):
        """Extract the minimum element (root) from the heap."""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store root to return
        root = self.heap[0]
        
        # Move last element to root and remove last element
        self.heap[0] = self.heap.pop()
        
        # Restore heap property
        self.heapify_down(0)
        
        return root
    
    def peek(self):
        """Return the minimum element without removing it."""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return the size of the heap."""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty."""
        return len(self.heap) == 0
    
    def __str__(self):
        return str([str(node) for node in self.heap])


class MaxHeap:
    """Max Heap implementation where parent nodes have larger frequencies than children."""
    
    def __init__(self):
        self.heap = []
    
    def _parent_index(self, index):
        """Get parent index for given index."""
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        """Get left child index for given index."""
        return 2 * index + 1
    
    def _right_child_index(self, index):
        """Get right child index for given index."""
        return 2 * index + 2
    
    def _swap(self, i, j):
        """Swap two elements in the heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, index):
        """Move element up the heap to maintain max heap property."""
        while index > 0:
            parent_idx = self._parent_index(index)
            if self.heap[index].frequency <= self.heap[parent_idx].frequency:
                break
            self._swap(index, parent_idx)
            index = parent_idx
    
    def heapify_down(self, index):
        """Move element down the heap to maintain max heap property."""
        while True:
            largest = index
            left_idx = self._left_child_index(index)
            right_idx = self._right_child_index(index)
            
            # Check if left child is larger
            if (left_idx < len(self.heap) and 
                self.heap[left_idx].frequency > self.heap[largest].frequency):
                largest = left_idx
            
            # Check if right child is larger
            if (right_idx < len(self.heap) and 
                self.heap[right_idx].frequency > self.heap[largest].frequency):
                largest = right_idx
            
            # If no change needed, break
            if largest == index:
                break
            
            self._swap(index, largest)
            index = largest
    
    def insert(self, node):
        """Insert a new node into the heap."""
        self.heap.append(node)
        self.heapify_up(len(self.heap) - 1)
    
    def extract(self):
        """Extract the maximum element (root) from the heap."""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store root to return
        root = self.heap[0]
        
        # Move last element to root and remove last element
        self.heap[0] = self.heap.pop()
        
        # Restore heap property
        self.heapify_down(0)
        
        return root
    
    def peek(self):
        """Return the maximum element without removing it."""
        return self.heap[0] if self.heap else None
    
    def size(self):
        """Return the size of the heap."""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty."""
        return len(self.heap) == 0
    
    def __str__(self):
        return str([str(node) for node in self.heap])