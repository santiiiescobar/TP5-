class TreeNode:
    def __init__(self, name, is_hero):
        self.name = name
        self.is_hero = is_hero
        self.left = None
        self.right = None
class MarvelTree:
    def __init__(self):
        self.root = None

    def insert(self, name, is_hero):
        self.root = self._insert(self.root, name, is_hero)

    def _insert(self, node, name, is_hero):
        if node is None:
            return TreeNode(name, is_hero)

        if name < node.name:
            node.left = self._insert(node.left, name, is_hero)
        elif name > node.name:
            node.right = self._insert(node.right, name, is_hero)

        return node

    def list_villains_alphabetically(self):
        self._list_villains_alphabetically(self.root)

    def _list_villains_alphabetically(self, node):
        if node:
            if not node.is_hero:
                self._list_villains_alphabetically(node.left)
                print(node.name)
                self._list_villains_alphabetically(node.right)

    def superheroes_with_C(self):
        self._superheroes_with_C(self.root)

    def _superheroes_with_C(self, node):
        if node:
            self._superheroes_with_C(node.left)
            if node.is_hero and node.name.startswith("C"):
                print(node.name)
            self._superheroes_with_C(node.right)

    def count_superheroes(self):
        return self._count_superheroes(self.root)

    def _count_superheroes(self, node):
        if node is None:
            return 0
        count = self._count_superheroes(node.left) + self._count_superheroes(node.right)
        if node.is_hero:
            count += 1
        return count

    def find_and_rename(self, incorrect_name, correct_name):
        self.root = self._find_and_rename(self.root, incorrect_name, correct_name)

    def _find_and_rename(self, node, incorrect_name, correct_name):
        if node is None:
            return None
        if node.name == incorrect_name:
            node.name = correct_name
        node.left = self._find_and_rename(node.left, incorrect_name, correct_name)
        node.right = self._find_and_rename(node.right, incorrect_name, correct_name)
        return node

    def list_superheroes_descending(self):
        self._list_superheroes_descending(self.root)

    def _list_superheroes_descending(self, node):
        if node:
            self._list_superheroes_descending(node.right)
            if node.is_hero:
                print(node.name)
            self._list_superheroes_descending(node.left)

marvel_tree = MarvelTree()
marvel_tree.insert("Iron Man", True)
marvel_tree.insert("Thor", True)
marvel_tree.insert("Loki", False)
marvel_tree.insert("Captain America", True)
marvel_tree.insert("Doctor Strange", True)
marvel_tree.insert("Black Widow", True)
marvel_tree.insert("Hulk", True)
marvel_tree.insert("Ultron", False)

print("Villanos ordenados alfabéticamente:")
marvel_tree.list_villains_alphabetically()

print("\nSuperhéroes que empiezan con 'C':")
marvel_tree.superheroes_with_C()

print("\nCantidad de superhéroes en el árbol:", marvel_tree.count_superheroes())

print("\nSuperhéroes y villanos antes de corregir 'Doctor Strange':")
marvel_tree.list_superheroes_descending()

marvel_tree.find_and_rename("Doctor Strange", "Doctor Strange")

print("\nSuperhéroes y villanos después de corregir 'Doctor Strange':")
marvel_tree.list_superheroes_descending()
