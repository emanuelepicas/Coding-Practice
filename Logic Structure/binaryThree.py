# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x        # Node value
        self.left = None    # Left child
        self.right = None   # Right child

def treeNodeToString(root):
    if not root:
        return "[]"         # Return empty list if tree is empty
    output = ""
    queue = [root]          # Queue for level-order traversal (BFS)
    current = 0
    while current != len(queue):
        node = queue[current]
        current += 1        # Move to the next node in the queue

        if not node:
            output += "null, "     # Append 'null' for None nodes
            continue

        output += str(node.val) + ", "    # Append node value to output
        queue.append(node.left)           # Enqueue left child
        queue.append(node.right)          # Enqueue right child
    # Remove trailing 'null, ' entries
    while output.endswith("null, "):
        output = output[:-6]
    # Remove the last ', ' and enclose in brackets
    return "[" + output[:-2] + "]"

def stringToTreeNode(input):
    input = input.strip()           # Remove leading/trailing whitespaces
    input = input[1:-1]             # Remove surrounding brackets
    if not input:
        return None                 # Return None if input is empty

    inputValues = [s.strip() for s in input.split(',')]  # Split input string into values
    root = TreeNode(int(inputValues[0]))    # Create root node
    nodeQueue = [root]                      # Queue for level-order traversal
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front += 1

        # Process left child
        item = inputValues[index]
        index += 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)    # Create left child
            nodeQueue.append(node.left)         # Enqueue left child

        if index >= len(inputValues):
            break

        # Process right child
        item = inputValues[index]
        index += 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)  # Create right child
            nodeQueue.append(node.right)        # Enqueue right child
    return root

def prettyPrintTree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        # Print right subtree
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    # Print current node
    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        # Print left subtree
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)

def main():
    # Sample inputs to test the code
    sample_inputs = [
        "[1, 2, 3, null, null, 4, 5]",
        "[1, null, 2, 3]",
        "[]",
        "[3,9,20,null,null,15,7]",
        "[1,2,2,3,4,4,3]"
    ]

    for input_line in sample_inputs:
        print(f"Input: {input_line}")
        # Convert string to binary tree
        node = stringToTreeNode(input_line)
        print("Binary Tree:")
        # Print the binary tree visually
        prettyPrintTree(node)
        # Convert binary tree back to string representation
        print("\nString Representation:", treeNodeToString(node))
        print("\n" + "-" * 40 + "\n")  # Separator for readability

if __name__ == '__main__':
    main()