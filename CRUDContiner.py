class CRUDContainer:
    def __init__(self):
        self.is_dict = True
        self.object_dict = {}

    def _next_index(self):
        int_keys = [key for key in self.object_dict.keys() if isinstance(key, int)]
        return (max(int_keys) + 1) if int_keys else 0

    def list(self):
        if not self.is_dict:
            return None
        for obj_key, obj_value in self.object_dict.items():
            print(f"\n{obj_key}: {obj_value}")
        return None

    def add(self, key, value=None):
        if not self.is_dict:
            return False
        if value is None:
            value = key
            key = self._next_index()
        if key is None or value is None:
            return False
        self.object_dict[key] = value
        return True

    def update(self, key, value):
        if key in self.object_dict:
            self.object_dict[key] = value
            return True
        return False

    def remove(self, key):
        return self.object_dict.pop(key, None) is not None

    def get(self, key):
        return self.object_dict.get(key)
    
    def size(self):
        return len(self.object_dict) if self.is_dict else 0
    
    def __len__(self):
        return self.size()