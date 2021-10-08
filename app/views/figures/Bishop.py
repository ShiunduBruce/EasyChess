import views.figures.Figure as Figure

class Bishop(Figure):
    def __init__(self, x, y):
        Figure.__init__(self, "D", x, y)