class Node:
    def __init__(self, data, branchings = []):
        self.branchings = branchings
        self.data = data
    def AddBranch(self, object):
        self.branchings += [Node(object)]
    def AddBud(self, object):
        self.branchings += object
