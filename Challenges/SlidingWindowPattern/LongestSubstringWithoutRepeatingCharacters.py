class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize window pointers and max length
        left = 0
        max_length = 0
        char_set = set()  # To track characters in current window
        
        # Move right pointer
        for right in range(len(s)):
            print(f"Right value {right}")
            # While we have a repeating character
            while s[right] in char_set:
                # Remove leftmost character and move left pointer
                char_set.remove(s[left])
                left += 1
            
            # Add current character to set
            char_set.add(s[right])
            
            # Update max length if current window is larger
            max_length = max(max_length, right - left + 1)
            
        return max_length

def visualize_sliding_window(s: str):
    solution = Solution()
    left = 0
    max_length = 0
    char_set = set()
    
    print(f"\nProcessing string: '{s}'")
    print("Window movement visualization:")
    
    for right in range(len(s)):
        print(f"\nStep {right + 1}:")
        
        # Show current character being processed
        print(f"Processing character: '{s[right]}'")
        
        # Handle repeating character
        while s[right] in char_set:
            print(f"Found repeat of '{s[right]}', removing '{s[left]}' from window")
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        current_length = right - left + 1
        
        # Visualize current window
        window_str = ""
        for i in range(len(s)):
            if i < left:
                window_str += f" {s[i]} "
            elif i >= left and i <= right:
                window_str += f"[{s[i]}]"
            else:
                window_str += f" {s[i]} "
        
        print(f"Current window: {window_str}")
        print(f"Window content: '{s[left:right+1]}'")
        print(f"Window length: {current_length}")
        
        if current_length > max_length:
            max_length = current_length
            print(f"New maximum length: {max_length}")
        
    return max_length

# Test cases
test_cases = [
    "abcabcbb",  # Classic case
    "pwwkew",    # Discontinuous substring
    "bbbbb",     # Repeating characters
    "dvdf"       # Tricky case
]

for test_string in test_cases:
    print("\n" + "="*50)
    result = visualize_sliding_window(test_string)
    print(f"\nFinal result for '{test_string}': {result}")