class CompressedVector:
    def __init__(self, compressed_form: List[tuple]):
        """
        Initialize compressed vector
        compressed_form: list of tuples (value, frequency)
        """
        self.data = compressed_form
    
    def dot_product(self, other: 'CompressedVector') -> int:
        """
        Calculate dot product with another compressed vector
        Time: O(n) where n is number of compressed pairs
        Space: O(1)
        """
        i = j = 0
        result = 0
        
        while i < len(self.data) and j < len(other.data):
            val1, freq1 = self.data[i]
            val2, freq2 = other.data[j]
            
            # Find overlapping frequency
            overlap = min(freq1, freq2)
            
            # Add to result
            result += val1 * val2 * overlap
            
            # Update frequencies
            freq1 -= overlap
            freq2 -= overlap
            
            # Move to next pair if frequency is exhausted
            if freq1 == 0:
                i += 1
            if freq2 == 0:
                j += 1
                
        return result

def visualize_dot_product():
    """
    Visualize the dot product calculation process
    """
    # Test cases
    test_cases = [
        ([(4,2), (5,1)], [(2,2), (3,1)]),  # [4,4,5] · [2,2,3]
        ([(1,3)], [(2,3)]),                 # [1,1,1] · [2,2,2]
        ([(2,2), (3,2)], [(1,2), (4,2)])   # [2,2,3,3] · [1,1,4,4]
    ]
    
    for v1_comp, v2_comp in test_cases:
        print("\n" + "="*50)
        print(f"Vector 1 (compressed): {v1_comp}")
        print(f"Vector 2 (compressed): {v2_comp}")
        
        # Create vectors
        v1 = CompressedVector(v1_comp)
        v2 = CompressedVector(v2_comp)
        
        # Calculate dot product with visualization
        i = j = 0
        result = 0
        step = 1
        
        while i < len(v1.data) and j < len(v2.data):
            val1, freq1 = v1.data[i]
            val2, freq2 = v2.data[j]
            
            print(f"\nStep {step}:")
            print(f"Comparing: ({val1}, {freq1}) and ({val2}, {freq2})")
            
            overlap = min(freq1, freq2)
            contribution = val1 * val2 * overlap
            result += contribution
            
            print(f"Overlap: {overlap}")
            print(f"Contribution: {val1} * {val2} * {overlap} = {contribution}")
            print(f"Running total: {result}")
            
            freq1 -= overlap
            freq2 -= overlap
            
            if freq1 == 0:
                i += 1
                print(f"Moving to next pair in vector 1")
            if freq2 == 0:
                j += 1
                print(f"Moving to next pair in vector 2")
                
            step += 1
        
        print(f"\nFinal dot product: {result}")

# Run visualization
if __name__ == "__main__":
    visualize_dot_product()