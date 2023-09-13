from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from ..functions import get_private_ip
from ..colors import font_family, font_size, color


def gruvbox_widgets_list():
    widgets_list = [
        widget.TextBox(
            text='',
            font=font_family,
            background=color['bg'],
            foreground=color['yellow'],
            padding=0,
            fontsize=30,
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=color['white'],
            background=color['bg']
        ),
        widget.GroupBox(
            font=font_family,
            fontsize=font_size,
            disable_drag=True,
            margin_y=3,
            margin_x=0,
            padding_x=8,
            dragable=False,
            active=color['white'],
            inactive=color['blue'],
            borderwidth=1,
            rounded=False,
            highlight_color=color['fg'],
            highlight_method='text',
            this_current_screen_border=color['yellow'],
            this_screen_border=color['red'],
            other_current_screen_border=color['white'],
            other_screen_border=color['green'],
            foreground=color['white'],
            background=color['bg'],
            decorations=[
                PowerLineDecoration(path='arrow_left')
            ]
        ),
        widget.CurrentLayout(
            fmt=' {}',
            foreground=color['white'],
            background=color['blue'],
            padding=5,
            decorations=[
                PowerLineDecoration(path='forward_slash')
            ],
        ),
        widget.Spacer(
            background=color['bg']
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=color['bg'],
            background=color['bg']
        ),
        widget.TextBox(
            decorations=[
                PowerLineDecoration(path='arrow_right')
            ]
        ),
        widget.TextBox(
            text=f'{get_private_ip()}',
            font=font_family,
            fontsize=font_size,
            padding=3,
            background=color['red'],
            foreground=color['bg'],
            decorations=[
                PowerLineDecoration(path='arrow_right')
            ]

        ),
        widget.Memory(
            foreground=color['bg'],
            background=color['white'],
            format='{MemUsed:.1f}/{MemTotal:.1f} GiB',
            measure_mem='G',
            padding=5,
            decorations=[
                PowerLineDecoration(path='arrow_right')
            ]
        ),
        widget.CPU(
            format='Cpu: {load_percent:.1f}%',
            font=font_family,
            fontsize=font_size,
            center_aligned=True,
            foreground=color['bg'],
            background=color['green'],
            decorations=[
                PowerLineDecoration(path='arrow_right')
            ]
        ),
        widget.Volume(
            foreground=color['white'],
            background=color['blue'],
            fmt='Vol:{}',
            padding=5,
            decorations=[
                PowerLineDecoration(path='arrow_right')
            ]
        ),
        widget.Systray(
            foreground=color['bg'],
            background=color['bg'],
            padding=2
        ),
        widget.Clock(
            foreground=color['white'],
            background=color['bg'],
            format='%H:%M %d/%b'
        ),
        widget.TextBox(
            text='',
            font=font_family,
            foreground=color['yellow'],
            background=color['bg'],
            padding=0,
            fontsize=30
        )
    ]
    return widgets_list
