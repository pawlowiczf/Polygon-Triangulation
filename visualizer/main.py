from .figures.line_segment import LineSegment
from .figures.polygon import Polygon
from .plot.plot import Plot

class Visualizer:
    def __init__(self):
        self.data = []
        self.plot_data = {}

    def add_title(self, title):
        self.plot_data['title'] = title

    def add_grid(self):
        self.plot_data['grid'] = True

    def axis_equal(self):
        self.plot_data['axis_equal'] = True

    def add_line_segment(self, data, **kwargs):
        line_segment = LineSegment(data, kwargs)
        self.data.append(line_segment)
        return line_segment

    def add_polygon(self, data, **kwargs):
        polygon = Polygon(data, kwargs)
        self.data.append(polygon)
        return polygon

    def clear(self):
        self.data = []
        self.plot_data = {}

    def show(self):
        Plot.show(self.plot_data, self.data)

    def save(self, filename='plot'):
        Plot.save(self.plot_data, self.data, filename)

    def show_gif(self, interval=256):
        gif = Plot.show_gif(self.plot_data, self.data, interval)
        return gif

    def save_gif(self, filename='animation', interval=256):
        Plot.save_gif(self.plot_data, self.data, interval, filename)
