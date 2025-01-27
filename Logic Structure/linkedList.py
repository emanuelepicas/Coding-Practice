# Definition for singly-linked list.
class ListNode(object):  # Uncommented the class definition
    def __init__(self, x):
        self.val = x
        self.next = None

import json

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def prettyPrintLinkedList(node):
    # Modified to work without sys.stdout and compatible with Python 3
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print("->".join(result) if result else "Empty LinkedList")

def main():
    # Sample inputs
    sample_inputs = [
        "[1,2,3,4,5]",
        "[]",
        "[10]",
        "[7,14,21,28]"
    ]

    for input_line in sample_inputs:
        print(f"Input: {input_line}")
        node = stringToListNode(input_line)
        print("Output: ", end="")
        prettyPrintLinkedList(node)
        print()  # Blank line for readability

if __name__ == '__main__':
    main()