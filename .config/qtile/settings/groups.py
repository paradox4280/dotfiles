from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.lazy import lazy

from .keys import mod, keys

groups = [Group(f'{i+1}', label='') for i in range(6)]
# groups = [Group(i) for i in '123456']

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod, 'shift'], i.name, lazy.window.togroup(i.name, switch_group=True))
        ]
    )

groups.append(
    ScratchPad(
        'scratchpad', [
            DropDown('term', 'alacritty', width=0.8, height=0.7, x=0.1, y=0.1, opacity=1),
            # DropDown('fm', 'pcmanfm', width=0.4, heigraht=0.5, x=0.3, y=0.1, opacity=0.5),
        ]
    )
)

keys.extend(
    [
        Key(['control'], 'Return', lazy.group['scratchpad'].dropdown_toggle('term')),
        # Key(['control'], 's', lazy.group['scratchpad'].dropdown_toggle('fm')),
    ]
)
