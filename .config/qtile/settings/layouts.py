from libqtile import layout
from libqtile.config import Match

from .colors import color

layout_config = {
    'margin': 10,
    'border_width': 2,
    'border_focus': color['white'],
    'border_normal': color['fg']
}

layouts = [
    layout.MonadTall(**layout_config),
    layout.MonadWide(**layout_config),
    layout.Matrix(**layout_config),
    layout.Zoomy(**layout_config),
    layout.Bsp(**layout_config),
    layout.Max(**layout_config),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(title='branchdialog'),
        Match(title='Open File'),
        Match(title='pinentry'),
        Match(wm_class='ssh-askpass'),
        Match(wm_class='lxpolkit'),
        Match(wm_class='Lxpolkit'),
        Match(wm_class='yad'),
        Match(wm_class='Yad'),
        Match(wm_class='Cairo-dock'),
        Match(wm_class='cairo-dock'),
    ],
    fullscreen_border_width=0,
    border_width=0
)
