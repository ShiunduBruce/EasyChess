import views.figures.Figure as Figure

class Knight(Figure):
    def __init__(self, x, y):
        Figure.__init__(self, "L", x, y)