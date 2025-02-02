class HashMapExamples:
    def __init__(self):
        # Initialize different types of hashmaps
        self.simple_map = {}  # Empty hashmap
        mapSimple = {}
        mapSimple["test"] = "test"
        self.count_map = {}   # For counting occurrences
        self.index_map = {}   # For storing indices
        self.list_map = {}    # For storing lists as values

    def demonstrate_basic_operations(self):
        """Basic HashMap Operations"""
        print("\n=== Basic HashMap Operations ===")
        
        # Adding key-value pairs
        hashmap = {}
        hashmap["name"] = "John"
        hashmap["age"] = 25
        hashmap["city"] = "New York"
        
        print(f"Initial HashMap: {hashmap}")
        
        # Accessing values
        print(f"Name: {hashmap['name']}")
        print(f"Age: {hashmap.get('age')}")  # Safe access with get()
        print(f"Country: {hashmap.get('country', 'Not Found')}")  # Default value if key not found
        
        # Updating values
        hashmap["age"] = 26
        print(f"Updated age: {hashmap['age']}")
        
        # Removing items
        removed_city = hashmap.pop("city")
        print(f"Removed city: {removed_city}")
        print(f"Updated HashMap: {hashmap}")

    def count_elements(self, arr: list) -> dict:
        """Count frequency of elements using HashMap"""
        print("\n=== Counting Elements ===")
        count_map = {}
        
        for num in arr:
            # Increment count or initialize to 1
            count_map[num] = count_map.get(num, 0) + 1
        
        print(f"Array: {arr}")
        print(f"Frequency Map: {count_map}")
        return count_map

    def store_indices(self, arr: list) -> dict:
        """Store indices of elements using HashMap"""
        print("\n=== Storing Indices ===")
        index_map = {}
        
        for i, num in enumerate(arr):
            # Store index for each number
            if num in index_map:
                index_map[num].append(i)
            else:
                index_map[num] = [i]
        
        print(f"Array: {arr}")
        print(f"Index Map: {index_map}")
        return index_map

    def two_sum_example(self, nums: list, target: int) -> list:
        """Two Sum problem using HashMap"""
        print("\n=== Two Sum Example ===")
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                result = [hashmap[complement], i]
                print(f"Found pair: {nums[result[0]]} + {nums[result[1]]} = {target}")
                return result
            hashmap[num] = i
        
        return []

    def group_by_category(self, items: list) -> dict:
        """Group items by category using HashMap"""
        print("\n=== Grouping Items ===")
        category_map = {}
        
        for item in items:
            category = item['category']
            if category not in category_map:
                category_map[category] = []
            category_map[category].append(item['name'])
        
        print(f"Items: {items}")
        print(f"Grouped by category: {category_map}")
        return category_map

def run_examples():
    examples = HashMapExamples()
    
    # Basic operations
    examples.demonstrate_basic_operations()
    
    # Counting elements
    arr1 = [1, 2, 3, 1, 2, 1, 3, 4]
    examples.count_elements(arr1)
    
    # Storing indices
    arr2 = [1, 2, 3, 1, 2, 1]
    examples.store_indices(arr2)
    
    # Two Sum example
    nums = [2, 7, 11, 15]
    target = 9
    examples.two_sum_example(nums, target)
    
    # Grouping items
    items = [
        {'name': 'apple', 'category': 'fruit'},
        {'name': 'banana', 'category': 'fruit'},
        {'name': 'carrot', 'category': 'vegetable'},
        {'name': 'orange', 'category': 'fruit'},
        {'name': 'broccoli', 'category': 'vegetable'}
    ]
    examples.group_by_category(items)

if __name__ == "__main__":
    run_examples()