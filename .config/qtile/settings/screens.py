from libqtile import bar
from libqtile.config import Screen

from .widget import widget

size = 30
opacity = 0.85
top_margin = [10, 10, 0, 10]
bottom_margin = [0, 10, 5, 10]


def init_screens(widget, size: int, opacity: float | int, margin: list | int) -> list:
    return [Screen(top=bar.Bar(widgets=widget, size=size, opacity=opacity, margin=margin))]


screens = init_screens(widget=widget, size=size, opacity=opacity, margin=top_margin)
