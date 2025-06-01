class ASTNode:
    def __init__(self, value, type):
        self.left = None
        self.right = None
        self.token = None
        self.type = type 
        self.value = value
        self.indentation = 0

    def createNode(self, value, type):
        t = ASTNode(value, type)
        return t

    def setType(self, type):
        self.type = type

    def setVal(self, value):
        self.value = value

    def getVal(self):
        return self.value

    def getType(self):
        return self.type