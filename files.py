class File:
    def __init__(self, path, value=''):
        self.path = path
        self.value = value
    def set(self):
        file = open(self.path, 'w')
        file.write(self.value)
        return file
    def get(self):
        file = open(self.path, 'r')
        return file
    def add(self):
        file = open(self.path, 'a')
        file.write(self.value)
        return file
