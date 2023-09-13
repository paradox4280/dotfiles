from .widgets.default_widget import default_widgets_list
from .widgets.gruvbox_widget import gruvbox_widgets_list
from .widgets.pokemon_widget import pokemon_widgets_list
from .widgets.rosepine_widget import rosepine_widgets_list

from .colors import font_family, font_size, color

widget = default_widgets_list()

widget_defaults = dict(
    font=font_family,
    fontsize=font_size,
    padding=2,
    background=color['bg']
)

extension_defaults = widget_defaults.copy()
