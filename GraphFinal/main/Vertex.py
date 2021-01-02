class Vertex(object):
    """description of class"""


    def __init__(self, label, edges = []):
        self.label = label
        self.edges = edges

    def __str__(self):
        return self.label, "\t\t", self.edges