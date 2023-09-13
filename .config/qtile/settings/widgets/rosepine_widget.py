from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from ..colors import color

powerline = {
    'decorations': [
        PowerLineDecoration(path='forward_slash')
    ]
}


def rosepine_widgets_list():
    return [
        widget.TextBox(
            text=' 󰣇 ',
            foreground=color['black'],
            background=color['green'],
            padding=2,
            fontsize=22,
            # mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(launcher)},
            **powerline
        ),
        widget.CurrentLayout(
            padding=1,
            foreground=color['black'],
            background=color['green'],
        ),
        widget.Sep(linewidth=0, padding=14, size_percent=40, background=color['green'],**powerline),
        widget.GroupBox(
            background=color['bg'],
            borderwidth=1,
            active=color['yellow'],
            inactive=color['magenta'],
            highlight_method='line',
            highlight_color=color['bg'],
            this_current_screen_border=color['yellow'],
            disable_drag=True,
            hide_unused=False,
            padding=10,
            spacing=5,
        ),
        # widget.WindowName(
        #     foreground=color['bluegray'],
        #     background=color['bg'],
        #     width=bar.CALCULATED,
        #     padding=10,
        #     **powerline
        # ),
        widget.Spacer(background=color['black']),
        widget.Wttr(
            location={
                'London': 'London',
                },
            # format='%l: %C, temp: %t, feels: %f',
            format='%l: %C %t',
            units='m',
            update_interval=30,
            padding=1,
            background=color['black'],
            foreground=color['fg'],
        ),
        widget.Spacer(background=color['black'], **powerline),
        widget.Systray(
            background=color['bg'],
            icon_size=16,
            padding=20,
        ),
        widget.Sep(linewidth=0, padding=14, size_percent=40, background=color['bg'], **powerline),
        widget.Clock(
            foreground=color['bg'],
            background=color['red'],
            padding=10,
            format='󱡼  %I:%M %p',
            timezone='Europe/London',
        ),
        widget.Clock(
            foreground=color['black'],
            background=color['red'],
            padding=10,
            format='  %I:%M %p '
        ),
        widget.TextBox(
            text='  ',
            foreground=color['black'],
            background=color['red'],
            padding=2,
            fontsize=22,
            # mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(power_menu)},
        ),
    ]
