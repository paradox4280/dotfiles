from libqtile.config import Key
from libqtile.command import lazy

from .path import home

mod = 'mod4'
alt = 'mod1'
mod2 = 'control'

browser = 'firefox'
terminal = 'alacritty'
file_manager = 'pcmanfm'

keys = [
    # WM KEYS
    Key([mod], 'q', lazy.window.kill()),
    Key([mod, alt], 'q', lazy.shutdown()),
    Key([mod], 'Return', lazy.spawn(terminal)),
    Key([mod, mod2], 'r', lazy.reload_config()),
    Key([mod], 'KP_Enter', lazy.spawn(terminal)),
    Key([mod], 'f', lazy.window.toggle_fullscreen()),

    # UTILS
    Key([mod, 'shift'], 'v', lazy.spawn('clipmenu')),
    Key([mod, mod2], 'v', lazy.spawn('clipdel -d .*')),
    Key([mod, 'shift'], 'd', lazy.spawn('rofi -show drun')),
    Key([mod2, 'shift'], 'l', lazy.spawn('betterlockscreen -l')),
    Key([alt, mod2], 's', lazy.spawn(f'{home}/scripts/system.sh')),
    Key([alt, mod2], 'v', lazy.spawn(f'{home}/scripts/start-virtual-machine.py')),

    # APPS
    Key([alt], 'f', lazy.spawn(browser)),
    # Key([mod, 'shift'], 'v', lazy.spawn('vscodium')),
    Key([mod, 'shift'], 'Return', lazy.spawn(file_manager)),

    # SUPER + SHIFT KEYS
    Key([mod, 'shift'], 'r', lazy.restart()),

    # CONTROL + ALT KEYS
    Key([alt, 'control'], 'o', lazy.spawn(f'{home}/scripts/picom-toggle.sh')),
    # Key([alt, 'control'], 'u', lazy.spawn('pavucontrol')),

    # SCREENSHOTS
    Key([], 'Print', lazy.spawn(f'flameshot full -p {home}/Pictures')),
    Key([mod, 'shift'], 's', lazy.spawn(f'flameshot gui -p {home}/Pictures')),

    ## MULTIMEDIA KEYS

    # INCREASE/DECREASE BRIGHTNESS
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl s +5%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl s 5%-')),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], 'XF86AudioMute', lazy.spawn(f'{home}/scripts/volume.sh mute')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn(f'{home}/scripts/volume.sh down')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn(f'{home}/scripts/volume.sh up')),

    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next')),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
    Key([], 'XF86AudioStop', lazy.spawn('playerctl stop')),

    # Key([], 'XF86AudioPlay', lazy.spawn('mpc toggle')),
    # Key([], 'XF86AudioNext', lazy.spawn('mpc next')),
    # Key([], 'XF86AudioPrev', lazy.spawn('mpc prev')),
    # Key([], 'XF86AudioStop', lazy.spawn('mpc stop')),

    # QTILE LAYOUT KEYS
    Key([mod], 'n', lazy.layout.normalize()),
    Key([mod], 'space', lazy.next_layout()),

    # CHANGE FOCUS
    Key([mod], 'Up', lazy.layout.up()),
    Key([mod], 'Down', lazy.layout.down()),
    Key([mod], 'Left', lazy.layout.left()),
    Key([mod], 'Right', lazy.layout.right()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'l', lazy.layout.right()),

    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, 'control'], 'l',
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, 'control'], 'Right',
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, 'control'], 'h',
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, 'control'], 'Left',
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, 'control'], 'k',
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, 'control'], 'Up',
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, 'control'], 'j',
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, 'control'], 'Down',
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, 'shift'], 'f', lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([mod, alt], 'k', lazy.layout.flip_up()),
    Key([mod, alt], 'j', lazy.layout.flip_down()),
    Key([mod, alt], 'l', lazy.layout.flip_right()),
    Key([mod, alt], 'h', lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, 'shift'], 'Up', lazy.layout.shuffle_up()),
    Key([mod, 'shift'], 'Down', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'Left', lazy.layout.swap_left()),
    Key([mod, 'shift'], 'Right', lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, 'shift'], 'space', lazy.window.toggle_floating()),
]
