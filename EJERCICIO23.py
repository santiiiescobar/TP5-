class Creature:
    def __init__(self, name, defeated_by=None, description=None, captured_by=None):
        self.name = name
        self.defeated_by = defeated_by
        self.description = description
        self.captured_by = captured_by

class TreeNode:
    def __init__(self, creature):
        self.creature = creature
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, creature):
        self.root = self._insert(self.root, creature)

    def _insert(self, node, creature):
        if node is None:
            return TreeNode(creature)

        if creature.name < node.creature.name:
            node.left = self._insert(node.left, creature)
        elif creature.name > node.creature.name:
            node.right = self._insert(node.right, creature)

        return node

    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(f"Criatura: {node.creature.name}")
            if node.creature.defeated_by:
                print(f"Derrotada por: {node.creature.defeated_by}")
            if node.creature.description:
                print(f"Descripción: {node.creature.description}")
            print()
            self.in_order_traversal(node.right)

    def level_order_traversal(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(f"Criatura: {node.creature.name}")
            if node.creature.defeated_by:
                print(f"Derrotada por: {node.creature.defeated_by}")
            if node.creature.description:
                print(f"Descripción: {node.creature.description}")
            print()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if node is None:
            return None
        if node.creature.name == name:
            return node.creature
        if name < node.creature.name:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    def update_defeated_by(self, name, defeated_by):
        creature = self.search(name)
        if creature:
            creature.defeated_by = defeated_by

creature_tree = Tree()

creatures = [
    Creature("Ceto", defeated_by="Teseo"),
    Creature("Tifón", defeated_by="Zeus"),
    Creature("Equidna", defeated_by=["Argos Panoptes", "Teseo"]),
    Creature("Dino", defeated_by="Atalanta"),
    Creature("Pefredo"),
    Creature("Enio", defeated_by="Heracles"),
    Creature("Escila", defeated_by="Cloto"),
    Creature("Caribdis", defeated_by="Láquesis"),
    Creature("Euríale", defeated_by="Átropos"),
    Creature("Esteno", defeated_by=["Minotauro de Creta", "Teseo"]),
    Creature("Medusa", defeated_by="Perseo"),
    Creature("Ladón", defeated_by=["Heracles", "Argos Panoptes", "Hermes"]),
    Creature("Águila del Cáucaso"),
    Creature("Quimera", defeated_by="Belerofonte"),
    Creature("Hidra de Lerna", defeated_by="Heracles"),
    Creature("León de Nemea", defeated_by="Heracles"),
    Creature("Esfinge", defeated_by="Edipo"),
    Creature("Dragón de la Cólquida"),
    Creature("Cerbero", defeated_by="Heracles"),
    Creature("Talos", defeated_by="Medea"),
    Creature("Sirenas"),
    Creature("Pitón", defeated_by="Apolo"),
    Creature("Cierva de Cerinea"),
    Creature("Basilisco"),
    Creature("Toro de Creta", defeated_by="Teseo"),
    Creature("Jabalí de Erimanto"),
]

for creature in creatures:
    creature_tree.insert(creature)

print("Listado inorden de las criaturas y quienes las derrotaron:")
creature_tree.in_order_traversal(creature_tree.root)

creature_tree.update_defeated_by("Ceto", "Teseo")
creature_tree.update_defeated_by("Pefredo", "Carcinos")
creature_tree.update_defeated_by("Águila del Cáucaso", "Aves del Estínfalo")
creature_tree.update_defeated_by("Cerbero", "Heracles")
creature_tree.update_defeated_by("Toro de Creta", "Teseo")

print("\nListado inorden de las criaturas y quienes las derrotaron después de actualizar:")
creature_tree.in_order_traversal(creature_tree.root)

print("\nMostrar toda la información de la criatura 'Talos':")
talos_info = creature_tree.search("Talos")
if talos_info:
    print(f"Criatura: {talos_info.name}")
    if talos_info.defeated_by:
        print(f"Derrotada por: {talos_info.defeated_by}")
    if talos_info.description:
        print(f"Descripción: {talos_info.description}")

heroes_and_gods = ["Zeus", "Heracles", "Teseo", "Belerofonte", "Edipo", "Perseo", "Apolo", "Medea", "Atalanta"]
defeated_counts = {hero: 0 for hero in heroes_and_gods}
for creature in creatures:
    if creature.defeated_by:
        if isinstance(creature.defeated_by, list):
            for hero in creature.defeated_by:
                if hero in heroes_and_gods:
                    defeated_counts[hero] += 1
        else:
            if creature.defeated_by in heroes_and_gods:
                defeated_counts[creature.defeated_by] += 1

top_heroes = sorted(defeated_counts.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nLos 3 héroes o dioses que derrotaron mayor cantidad de criaturas:")
for hero, count in top_heroes:
    print(f"{hero}: {count} criaturas derrotadas")

print("\nCriaturas derrotadas por Heracles:")
for creature in creatures:
    if creature.defeated_by == "Heracles":
        print(creature.name)

print("\nCriaturas que no han sido derrotadas:")
for creature in creatures:
    if creature.defeated_by is None:
        print(creature.name)

creature_tree.update_defeated_by("Aves del Estínfalo", "Heracles")

ladon_info = creature_tree.search("Ladón")
if ladon_info:
    ladon_info.name = "Dragón Ladón"

def remove_creatures(node):
    if node is not None:
        if node.creature.name in ["Basilisco", "Sirenas"]:
            return None
        node.left = remove_creatures(node.left)
        node.right = remove_creatures(node.right)
        return node

creature_tree.root = remove_creatures(creature_tree.root)

print("\nListado por nivel del árbol:")
creature_tree.level_order_traversal()

print("\nCriaturas capturadas por Heracles:")
for creature in creatures:
    if creature.captured_by == "Heracles":
        print(creature.name)
