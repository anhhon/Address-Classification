class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.
        self.is_terminate = False


def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character through all children of the present `node`
        for child in node.children:
            if child.char == char:
                # Point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it in the children nodes -> add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # Point node to the new child
            node = new_node
    # Mark it as the end of a word.
    node.is_terminate = True


def find_prefix(root, prefix: str) -> bool:
    """
    Check and return if the prefix exsists in any of the words we added so far
    """
    node = root
    # If the root node has no children, then return False (Empty Trie).
    if not root.children:
        return False
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False
    return node.is_terminate

if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "Hà Nội")
    add(root, 'Hà Nam')
    add(root, 'Quảng Nam')

    print(find_prefix(root, 'Hà'))
    print(find_prefix(root, 'Nội'))
    print(find_prefix(root, 'Hà Nội'))
    print(find_prefix(root, 'Quảng Nam'))
    print(find_prefix(root, 'Nam'))