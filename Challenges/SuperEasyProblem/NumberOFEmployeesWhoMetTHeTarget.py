class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        """
        Count employees who worked at least target hours
        
        Time Complexity: O(n) where n is number of employees
        Space Complexity: O(1)
        """
        return sum(1 for hour in hours if hour >= target)
    
    # Alternative more verbose solution
    def numberOfEmployeesWhoMetTarget_verbose(self, hours: List[int], target: int) -> int:
        count = 0
        for hours_worked in hours:
            if hours_worked >= target:
                count += 1
        return count

def visualize_process(hours: List[int], target: int):
    """
    Visualize how we check each employee's hours
    """
    print(f"\nChecking employees' hours:")
    print(f"Target hours: {target}")
    print("\nProcess:")
    
    count = 0
    for i, hours_worked in enumerate(hours):
        print(f"\nEmployee {i}:")
        print(f"Hours worked: {hours_worked}")
        
        if hours_worked >= target:
            count += 1
            print(f"✓ Met target ({hours_worked} >= {target})")
            print(f"Count increased to {count}")
        else:
            print(f"✗ Did not meet target ({hours_worked} < {target})")
    
    print(f"\nFinal count of employees who met target: {count}")
    return count

# Test cases
test_cases = [
    {
        'hours': [0,1,2,3,4],
        'target': 2,
        'description': "Example 1 - Mixed hours"
    },
    {
        'hours': [5,1,4,2,2],
        'target': 6,
        'description': "Example 2 - No one meets target"
    },
    {
        'hours': [1,2,3,4,5],
        'target': 1,
        'description': "All meet target"
    },
    {
        'hours': [0,0,0],
        'target': 1,
        'description': "No one worked"
    },
    {
        'hours': [10],
        'target': 5,
        'description': "Single employee"
    }
]

def run_tests():
    solution = Solution()
    
    for i, case in enumerate(test_cases, 1):
        print("\n" + "="*60)
        print(f"Test Case {i}: {case['description']}")
        
        hours = case['hours']
        target = case['target']
        
        # Visualize the process
        expected = visualize_process(hours, target)
        
        # Get solution result
        result = solution.numberOfEmployeesWhoMetTarget(hours, target)
        
        # Verify results
        print(f"\nExpected: {expected}")
        print(f"Got: {result}")
        assert result == expected, f"Test case failed! Expected {expected}, got {result}"
        print("✓ Test passed")

if __name__ == "__main__":
    run_tests()