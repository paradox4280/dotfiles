from qtile_extras import widget
from ..colors import font_family, font_size, color


def default_widgets_list():
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
