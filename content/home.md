---
title: "Home"
date: 2022-04-30T18:34:51+05:30
description: "A full-featured, hackable tiling window manager written and configured in Python"
---

```py

    from libqtile.config import Key, Screen, Group, Drag, Click
    from libqtile.command import lazy
    from libqtile import layout, bar, widget

    try:
        from typing import List  # noqa: F401
    except ImportError:
        pass

    mod = "mod4"

    keys = [
        # Switch between windows in current stack pane
        Key([mod], "k", lazy.layout.down()),
        Key([mod], "j", lazy.layout.up()),

        # Move windows up or down in current stack
        Key([mod, "control"], "k", lazy.layout.shuffle_down()),
        Key([mod, "control"], "j", lazy.layout.shuffle_up()),

        # Switch window focus to other pane(s) of stack
        Key([mod], "space", lazy.layout.next()),

        # Swap panes of split stack
        Key([mod, "shift"], "space", lazy.layout.rotate()),

        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
        Key([mod], "Return", lazy.spawn("xterm")),

        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout()),
        Key([mod], "w", lazy.window.kill()),

        Key([mod, "control"], "r", lazy.restart()),
        Key([mod, "control"], "q", lazy.shutdown()),
        Key([mod], "r", lazy.spawncmd()),
    ]

    groups = [Group(i) for i in "asdfuiop"]

    for i in groups:
        keys.extend([
            # mod1 + letter of group = switch to group
            Key([mod], i.name, lazy.group[i.name].toscreen()),

            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ])

    layouts = [
        layout.Max(),
        layout.Stack(num_stacks=2)
    ]

    widget_defaults = dict(
        font=&#x27;sans&#x27;,
        fontsize=12,
        padding=3,
    )
    extension_defaults = widget_defaults.copy()

    screens = [
        Screen(
            bottom=bar.Bar(
                [
                    widget.GroupBox(),
                    widget.Prompt(),
                    widget.WindowName(),
                    widget.TextBox("default config", name="default"),
                    widget.Systray(),
                    widget.Clock(format=&#x27;%Y-%m-%d %a %I:%M %p&#x27;),
                ],
                24,
            ),
        ),
    ]

    # Drag floating layouts.
    mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front())
    ]

    dgroups_key_binder = None
    dgroups_app_rules = []  # type: List
    main = None
    follow_mouse_focus = True
    bring_front_click = False
    cursor_warp = False
    floating_layout = layout.Floating(float_rules=[
        {&#x27;wmclass&#x27;: &#x27;confirm&#x27;},
        {&#x27;wmclass&#x27;: &#x27;dialog&#x27;},
        {&#x27;wmclass&#x27;: &#x27;download&#x27;},
        {&#x27;wmclass&#x27;: &#x27;error&#x27;},
        {&#x27;wmclass&#x27;: &#x27;file_progress&#x27;},
        {&#x27;wmclass&#x27;: &#x27;notification&#x27;},
        {&#x27;wmclass&#x27;: &#x27;splash&#x27;},
        {&#x27;wmclass&#x27;: &#x27;toolbar&#x27;},
        {&#x27;wmclass&#x27;: &#x27;confirmreset&#x27;},  # gitk
        {&#x27;wmclass&#x27;: &#x27;makebranch&#x27;},  # gitk
        {&#x27;wmclass&#x27;: &#x27;maketag&#x27;},  # gitk
        {&#x27;wname&#x27;: &#x27;branchdialog&#x27;},  # gitk
        {&#x27;wname&#x27;: &#x27;pinentry&#x27;},  # GPG key password entry
        {&#x27;wmclass&#x27;: &#x27;ssh-askpass&#x27;},  # ssh-askpass
    ])
    auto_fullscreen = True
    focus_on_window_activation = "smart"

    # XXX: Gasp! We&#x27;re lying here. In fact, nobody really uses or cares about this
    # string besides java UI toolkits; you can see several discussions on the
    # mailing lists, github issues, and other WM documentation that suggest setting
    # this string if your java app doesn&#x27;t work correctly. We may as well just lie
    # and say that we&#x27;re a working one by default.
    #
    # We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
    # java that happens to be on java&#x27;s whitelist.
    wmname = "LG3D"

    dpi_scale = 1.0
```
