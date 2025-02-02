class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        """
        Find maximum number of words in any sentence
        
        Time Complexity: O(n * m) where n is number of sentences and m is max sentence length
        Space Complexity: O(1)
        """
        return max(len(sentence.split()) for sentence in sentences)

    # Alternative solution using loop (more verbose but easier to understand)
    def mostWordsFound_verbose(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            # Split sentence into words and count them
            word_count = len(sentence.split())
            # Update maximum if current count is larger
            max_words = max(max_words, word_count)
            
        return max_words

def visualize_word_counting(sentences: List[str]):
    """
    Visualize how we count words in each sentence
    """
    print("Processing sentences:")
    max_words = 0
    
    for i, sentence in enumerate(sentences, 1):
        # Split sentence into words
        words = sentence.split()
        word_count = len(words)
        
        print(f"\nSentence {i}: '{sentence}'")
        print(f"Words: {words}")
        print(f"Word count: {word_count}")
        
        # Update maximum
        if word_count > max_words:
            max_words = word_count
            print(f"New maximum found: {max_words}")
    
    print(f"\nFinal maximum word count: {max_words}")
    return max_words

# Test cases
test_cases = [
    # Example 1
    ["alice and bob love leetcode", "i think so too", 
     "this is great thanks very much"],
    
    # Example 2
    ["please wait", "continue to fight", "continue to win"],
    
    # Additional test cases
    ["hello world", "hello"],  # Different lengths
    ["a", "b c", "d e f"],     # Increasing words
    ["one two three four"]     # Single sentence
]

def run_tests():
    solution = Solution()
    
    for i, sentences in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}:")
        print(f"Input sentences: {sentences}")
        
        # Visualize the process
        print("\nDetailed process:")
        max_words = visualize_word_counting(sentences)
        
        # Get solution result
        result = solution.mostWordsFound(sentences)
        
        # Verify results
        print(f"\nExpected: {max_words}")
        print(f"Got: {result}")
        assert result == max_words, f"Test case failed! Expected {max_words}, got {result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()