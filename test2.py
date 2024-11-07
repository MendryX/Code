from typing import Optional

class Fish:
    def __init__(self, name: str, species: str, value: int):
        self.name = name
        self.species = species
        self.value = value

class Node:
    def __init__(self, fish: Fish):
        self.fish = fish
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class Record:
    def __init__(self):
        self._first: Optional[Node] = None
        self._last: Optional[Node] = None
    
    def append(self, fish: Fish) -> None:
        node = Node(fish)
        if self._first is None:
            self._first = node
            self._last = node
            return
        self._last.next = node
        node.prev = self._last
        self._last = node

    def pop(self) -> Optional[Fish]:
        if self._first is None:
            return None
        node = self._last
        if self._first is self._last:
            self._first = None
            self._last = None
            return node.fish
        node.prev.next = None
        self._last = node.prev
        return node.fish
        
        
    
    def popleft(self) -> Optional[Fish]:
        if self._first is None:
            return None
        node = self._first
        if self._first is self._last:
            self._first = None
            self._last = None
            return node.fish
        node.next.prev = None
        self._first = node.next
        return node.fish
        

def is_valid(record: Record) -> bool:

    if record._first is None and record._last is None:
        return True
    
    if (record._first is None) is not (record._last is None):
        return False

    def count_nodes(head: Node):
        if head is None:
            return 0
        return 1 + count_nodes(head.next)
    
    # check prvního a posledního uzlu
    if record._first.prev is not None or record._last.next is not None:
        return False
        
    dl_list = record._first   
    while dl_list:
        # pokud není první uzel v pořádku
        if dl_list is record._first:
            if dl_list.next is not None: 
                if dl_list.next.prev is None or dl_list.next.prev is not dl_list:
                    return False
            elif dl_list.next is None and count_nodes(record._first) == 1:
                return True
        
        # pokud není poslední uzel v pořádku
        if dl_list is record._last and (dl_list.prev is None or dl_list.prev.next is not dl_list):
            return False

        # pokud je uzel uprostřed    
        if dl_list.next is not None and dl_list.prev is not None:
            if dl_list.next.prev is None or dl_list.next.prev is not dl_list: # pokud jsou zpětné pointery na None nebo jiný uzel
                return False
            else:
                dl_list = dl_list.next

        if dl_list is record._first or dl_list is record._last:
            dl_list = dl_list.next   

    x = count_nodes(record._first)
    y = record._first

    while x > 0:
        try:
            y = y.next
        except AttributeError:
            return False
        x -= 1
    if y is None and x == 0:
        return True
    elif y is not None:
        return False
# Testy:
