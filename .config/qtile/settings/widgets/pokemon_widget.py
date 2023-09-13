from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from ..colors import font_family, font_size, color


def pokemon_widgets_list():
    widgets_list = [
        # widget.Clock(
        #     format=' %H:%M ',
        #     background=color['yellow'],
        #     foreground=color['dark'],
        #     mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('fish -c "~/.config/qtile/time.sh"')}
        # ),
        # widget.TextBox(
        #     background=color['blue'],
        #     foreground=color['black'],
        #     text='',
        #     fontsize=22,
        #     markup=True
        # ),
        widget.GroupBox(
            background=color['blue'],
            active=color['yellow'],
            inactive=color['purple'],
            border_width=1,
            disable_drag=True,
            padding=0,
            highlight_method='line',
            highlight_color=color['blue'],
            fontsize=font_size
        ),
        widget.TextBox(
            background=color['blue'],
            foreground=color['black'],
            text=' ',
            fontsize=22,
            markup=True,
            padding=-4,
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.WindowName(
            background=color['red'],
            foreground=color['dark'],
            padding=10,
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.TextBox(
            text='  ',
            fontsize=17,
            font='HeavyData Nerd Font',
            background=color['cyan'],
            foreground=color['purple']
        ),
        widget.CPU(
            background=color['cyan'],
            foreground=color['dark'],
            format='{load_percent}%  ',
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.TextBox(
            text=' ﬙ ',
            fontsize=17,
            font='HeavyData Nerd Font',
            background=color['pink'],
            foreground=color['purple']
        ),
        widget.Memory(
            background=color['pink'],
            foreground=color['dark'],
            format='{MemUsed:.0f}MB  ',
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.TextBox(
            text=' 墳 ',
            fontsize=17,
            font='HeavyData Nerd Font',
            background=color['blue'],
            foreground=color['purple']
        ),
        widget.Volume(
            background=color['blue'],
            foreground=color['dark'],
            update_interval=0.1,
            step=5,
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.TextBox(
            background=color['blue'],
            foreground=color['black'],
            text='  ',
            fontsize=22,
            markup=True,
            padding=-4,
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.TextBox(
            text='  ',
            fontsize=17,
            font='HeavyData Nerd Font',
            background=color['green'],
            foreground=color['purple']
        ),
        widget.NvidiaSensors(
            background=color['green'],
            foreground=color['dark'],
            format='{temp}°C  ',
            treshhold=90,
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.TextBox(
            text=' 杖 ',
            fontsize=18,
            font='HeavyData Nerd Font',
            background=color['cream'],
            foreground=color['purple']
        ),
        widget.Wttr(
            background=color['cream'],
            foreground=color['dark'],
            format='%f  ',
            location={'Stanceni': 'Stanceni'},
            units='m',
            padding=4,
            update_interval=7200
        ),
        widget.TextBox(
            background=color['cream'],
            foreground=color['black'],
            text='  ',
            fontsize=22,
            markup=True,
            padding=-4,
            decorations=[
                PowerLineDecoration(path='rounded_right')
            ]
        ),
        widget.Clock(
            format=' %d.%m %a ',
            background=color['orange'],
            foreground=color['dark']
        ),
    ]
    return widgets_list
