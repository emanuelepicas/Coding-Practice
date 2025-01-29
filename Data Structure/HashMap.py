class HashMap:
    def __init__(self):
        self.map = {}
    
    def put(self, key, value):
        self.map[key] = value
    
    def get(self, key):
        return self.map.get(key)
    
    def delete(self, key):
        if key in self.map:
            del self.map[key]
    
    def display(self):
        return str(self.map)

# Visual Example:
"""
Initial: {}
After put("name", "John"): {"name": "John"}
After put("age", 25): {"name": "John", "age": 25}
After delete("age"): {"name": "John"}
"""

# Usage:
hm = HashMap()
hm.put("name", "John")
hm.put("age", 25)
print(hm.get("name"))  # "John"
hm.delete("age")
print(hm.display())  # "{'name': 'John'}"