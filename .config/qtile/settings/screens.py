from libqtile import bar
from libqtile.config import Screen

from .widgets import init_widgets_list, gruvbox_widgets_list

bar_position = 'top'


def top_init_screens() -> list:
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), size=30, opacity=1, margin=[10, 10, 0, 10]))]


def bottom_init_screens() -> list:
    return [Screen(bottom=bar.Bar(widgets=gruvbox_widgets_list(), size=30, opacity=0.85, margin=[0, 10, 5, 10]))]


def _bar_position(position: str):
    if position == 'top':
        return top_init_screens()
    else:
        return bottom_init_screens()


screens = _bar_position(bar_position)
