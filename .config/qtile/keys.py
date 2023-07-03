import os

from libqtile.config import Drag, Group, Key, ScratchPad, DropDown
from libqtile.command import lazy

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

myTerm = "alacritty" # My terminal of choice

keys = [
    # SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "KP_Enter", lazy.spawn('alacritty')),
    Key([mod], "x", lazy.shutdown()),

    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn('pcmanfm')),
    Key([mod, "shift"], "d", lazy.spawn('rofi -show')),
    Key([mod], "r", lazy.spawn(home + '/.config/rofi/bin/powermenu')),
    # Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#ff1493' -sb '#ff1493' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=15'")),
    # Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),

    # CONTROL + ALT KEYS
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),

    # ALT + ... KEYS
    Key(["mod1"], "f", lazy.spawn('firefox')),
    Key(["mod1"], "m", lazy.spawn('pcmanfm')),

    # CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),

    # SCREENSHOTS
    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),

    ## MULTIMEDIA KEYS

    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- ")),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("pamixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
    # Key([], "XF86AudioNext", lazy.spawn("mpc next")),
    # Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
    # Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    # CUSTOM
    Key([mod, "shift"], "c", lazy.spawn("vscodium")),
    Key([mod, "shift"], "s", lazy.spawn("/run/media/flu/DATA/Emu/ryujinx-1.1.866-linux_x64/Ryujinx")),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        
        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name))
        ]
    )

# ScratchPads
groups.append(
    ScratchPad(
        'scratchpad', [
            DropDown('term', 'alacritty', width=0.8, height=0.7, x=0.1, y=0.1, opacity=1),
            DropDown('fm', 'pcmanfm', width=0.4, heigraht=0.5, x=0.3, y=0.1, opacity=0.5),
            DropDown('rn', 'ranger', width=0.8, height=0.7, x=0.1, y=0.1, opacity=1),
        ]
    )
)

# Extend keys for scratchPad
keys.extend(
    [
        Key(["control"], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
        Key(["control", "shift"], "Return", lazy.group['scratchpad'].dropdown_toggle('rn')),
        # Key(["control"], "s", lazy.group['scratchpad'].dropdown_toggle('fm')),
    ]
)

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size())
]