import os
import subprocess

from libqtile import bar, widget, hook
from libqtile.config import Screen

from keys import keys, groups, mouse
from layouts import layouts, floating_layout

home = os.path.expanduser('~')

# Widgets
widget_defaults = dict(
    font="Cantarell Bold",
    fontsize=14,
    padding=6,
)

extension_defaults = widget_defaults.copy()

dark = {
    "background": "2e3440",
    "foreground": "f8f8f2",
    "black":      "5c6370",
    "red":        "e06c75",
    "green":      "98c379",
    "yellow":     "d19a66",
    "blue":       "61afef",
    "magenta":    "c678dd",
    "cyan":       "56b6c2",
    "white":      "828791",
    "back":       "2e3440",
    "fore":       "d8dee9",
    "select":     "81a1c1",
    "highlight":  "ebcb8b",
    "urgent":     "bf616a",
    "on":         "c679FF",
    "off":        "212B30",
    "BG":         "212B30",
    "BG1":        "263035",
    "BG2":        "2B353A",
    "BG3":        "303A3F",
    "BG4":        "353F44",
    "BG5":        "3A4449",
    "BG6":        "3F494E"
}

theme = dark

def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            font="Font Awesome 6 Free Solid",
            highlight_method="block",
            fmt="{}",
            this_current_screen_border=theme["on"],
            #this_other_screen_border=theme["blue"],
            #this_current_screen=theme["background"],
            block_highlight_text_color=theme["background"],
            inactive=theme["black"],
            background=theme["BG1"],
            borderwidth=0,
            rounded=True,
            padding_x=10,
            padding_y=8,
            margin_x=0
            #margin=0
        ),

        widget.WindowName(
            fmt='  {}',
            font="JetBrainsMono NL Nerd Font",
            fontsize=13,
            background=theme["BG"],
            center_aligned=True
        ),

        widget.Net(
            # interface="wlan0",
            format=" {down} ↓/↑{up}",
            prefix="k",
            background = theme["BG1"],
            foreground=theme["red"],
            font="JetBrainsMono NL Nerd Font",
            fontsize=14,
            center_aligned=True,
        ),

        widget.Memory(
            measure_mem="G",
            format="{MemUsed:.1f}/{MemTotal:.1f} GiB",
            background=theme["background"],
            foreground=theme["green"]
        ),

        widget.CPU(
            format="{load_percent:.1f}%",
            background=theme["background"],
            foreground=theme["yellow"]
        ),

        widget.CurrentLayout(
            background=theme["fore"],
            foreground=theme["back"],
            fontsize=13
        ),

        widget.CheckUpdates(
            distro="Arch",
            font="JetBrainsMono NL Nerd Font",
            fontsize=14,
            dislpay_format = '{updates}',
            no_update_string="Up To Date",
            colour_no_updates=theme["white"],
            colour_have_updates=theme["red"],
            background=theme["BG2"],
            foreground=theme["magenta"],
            center_aligned=True
        ),

        widget.Backlight(
            backlight_name='intel_backlight',
            brightnessfile='brightness',
            max_brightness_file='max_brightness',
            background = theme["BG4"],
            foreground=theme["cyan"],
            font="JetBrainsMono NL Nerd Font",
            fmt=' {}',
            fontsize=14,
            center_aligned=True
        ),

        widget.Clock(
            format="%d-%b %I:%M %p",
            background=theme["BG2"],
            foreground=theme["magenta"],
        ),

        widget.Systray(
            fontsize=12,
            background=theme["BG"],
            center_aligned=True
        ),
    ]
    return widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), size=30, opacity=0.85))]

screens = init_screens()

dgroups_key_binder = None
dgroups_app_rules = []

main = None

@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus" # or smart
wmname = "LG3D"
