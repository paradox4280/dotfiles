from libqtile import widget

from .functions import get_private_ip
from .colors import font_family, font_size, color


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            padding=6,
            linewidth=0,
            background=color['bg']
        ),
        widget.GroupBox(
            font=font_family,
            fontsize=font_size,
            disable_drag=True,
            dragable=False,
            rounded=False,
            hide_unsed=False,
            use_mouse_wheel=False,
            spacing=1,
            margin_y=3,
            margin_x=0,
            padding_x=8,
            borderwidth=1,
            active=color['white'],
            inactive=color['blue'],
            highlight_method='text',
            highlight_color=[color['fg'], color['yellow']],
            block_highlight_text_color=color['white'],
            this_current_screen_border=color['yellow'],
            foreground=color['blue'],
            background=color['bg']
        ),
        widget.CurrentLayout(
            fmt=' {}',
            padding=0
        ),
        widget.Spacer(
            background=color['bg']
        ),
        widget.CPU(
            format='Cpu: {load_percent:.1f}%',
            font=font_family,
            fontsize=font_size,
            center_aligned=True,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.ThermalZone(
            format=' {temp}°C',
            zone='/sys/class/thermal/thermal_zone0/temp'
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        # widget.Net(
        #     interface='wlo1',
        #     format=' {interface}: {down} ↓↑ {up}',
        #     update_interval=1.0,
        # ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.Memory(
            format='󰍛 {MemUsed:.1f}/{MemTotal:.1f} GiB',
            measure_mem='G',
            padding=5,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.Volume(
            fmt='Vol:{}',
            padding=5,
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.CheckUpdates(
            distro='Arch',
            font=font_family,
            fontsize=font_size,
            dislpay_format='{updates}',
            no_update_string='Up To Date',
            colour_no_updates=color['white'],
            colour_have_updates=color['red'],
            background=color['bg'],
            foreground=color['fg'],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=color['bg']
        ),
        widget.Systray(
            background=color['bg'],
            foreground=color['fg']
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=color['bg']
        ),
        widget.Clock(
            format='%I:%M %d/%b',
            update_interval=60.0,
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=color['bg']
        ),
    ]
    return widgets_list


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
            background=color['bg']
        ),
        widget.TextBox(
            text='',
            font=font_family,
            background=color['blue'],
            foreground=color['bg'],
            padding=0,
            fontsize=30,
        ),
        widget.CurrentLayout(
            fmt=' {}',
            foreground=color['white'],
            background=color['blue'],
            padding=5
        ),
        widget.TextBox(
            text='',
            font=font_family,
            background=color['bg'],
            foreground=color['blue'],
            padding=0,
            fontsize=30
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
            # text='',
            text='',
            font=font_family,
            background=color['bg'],
            foreground=color['red'],
            padding=0,
            fontsize=37
        ),
        widget.TextBox(
            text=f'{get_private_ip()}',
            font=font_family,
            fontsize=font_size,
            padding=3,
            background=color['red'],
            foreground=color['bg']

        ),
        widget.TextBox(
            text='',
            font=font_family,
            background=color['red'],
            foreground=color['white'],
            padding=0,
            fontsize=30
        ),
        widget.Memory(
            foreground=color['bg'],
            background=color['white'],
            format='{MemUsed:.1f}/{MemTotal:.1f} GiB',
            measure_mem='G',
            padding=5
        ),
        widget.TextBox(
            text='',
            font=font_family,
            background=color['white'],
            foreground=color['green'],
            padding=0,
            fontsize=30
        ),
        widget.CPU(
            format='Cpu: {load_percent:.1f}%',
            font=font_family,
            fontsize=font_size,
            center_aligned=True,
            foreground=color['bg'],
            background=color['green']
        ),
        widget.TextBox(
            text='',
            font=font_family,
            background=color['green'],
            foreground=color['blue'],
            padding=0,
            fontsize=30
        ),
        widget.Volume(
            foreground=color['white'],
            background=color['blue'],
            fmt='Vol:{}',
            padding=5
        ),
        widget.TextBox(
            text='',
            font=font_family,
            background=color['blue'],
            foreground=color['bg'],
            padding=0,
            fontsize=30
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


widget_defaults = dict(
    font=font_family,
    fontsize=font_size,
    padding=2,
    background=color['bg']
)

extension_defaults = widget_defaults.copy()
