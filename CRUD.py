class CRUDContainer:
    def __init__(self):
        self.is_array = True
        self.object_array = []

    def list(self):
        if not self.is_array:
            return None
        for object_element in self.object_array:
            print(f"\n{object_element}")
        return None
    
    def add(self, object_element):
        if not self.is_array or object_element is None:
            return False
        self.object_array.append(object_element)
        return True

    def update(self, index, object_element):
        if not self.is_array or index is None or object_element is None:
            return False
        try:
            self.object_array[index] = object_element
            return True
        except IndexError:
            return False

    def remove(self, index):
        if not self.is_array or index is None:
            return False
        try:
            self.object_array.pop(index)
            return True
        except IndexError:
            return False
    
    def get(self, index):
        if not self.is_array:
            return None
        try:
            return self.object_array[index]
        except IndexError:
            return None
    
    def size(self):
        return len(self.object_array) if self.is_array else 0
    
    def __len__(self):
        return self.size()