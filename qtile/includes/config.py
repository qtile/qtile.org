from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

MOD = 'mod4'

screens = [Screen(
    top=bar.Bar([
        widget.GroupBox(),
        widget.WindowName(),
        widget.Systray(),
        widget.Clock('%a %d %b %I:%M %p'),
    ], size=30)
)]

keys = [
    Key([MOD, 'control'], 'r', lazy.restart()),
    Key([MOD, 'control'], 'q', lazy.shutdown()),

    Key([MOD], 'w', lazy.window.kill()),
    Key([MOD], 'f', lazy.window.toggle_floating()),

    Key([MOD], 'Left', lazy.screen.prevgroup()),
    Key([MOD], 'Right', lazy.screen.nextgroup()),

    Key([MOD], 'Up', lazy.layout.next()),
    Key([MOD], 'Down', lazy.layout.previous()),
    Key([MOD], 'Tab', lazy.nextlayout()),
]

groups = []
for i in range(1, 10):
    groups.append(Group(i))
    keys.append(Key([MOD], i, lazy.group[i].toscreen()))
    keys.append(Key([MOD, 'MOD1'], i, lazy.window.togroup(i)))

layouts = [
    layout.Stack(stacks=2, border_width=1),
    layout.Max(),
]
