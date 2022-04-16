# Archivo de configuración de Qtile
# Ultima actualización 19/3/2022

# Importaciones
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

# Atajos de teclado
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.spawn("rofi -show run"), desc="Show rofi menu"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Control del volumen por teclado
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Control brillo por teclado
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Abrir programas
    Key([mod], "o", lazy.spawn("google-chrome-stable"), desc="Abrir navegador"),
    Key([mod], "c", lazy.spawn("code"), desc="Abrir code"),
    Key([mod], "z", lazy.spawn("okular"), desc="Abrit okular"),
    Key([mod], "x", lazy.spawn("rofi -show"), desc="Abre rofi en modo mostrar"),
    Key([mod], "n", lazy.spawn("notepadqq"), desc="Abre notepadqq"),
    Key([mod], "v", lazy.spawn("thunar"), desc="Abre thunar")
]

# Escritoios
escritorios = {
    1: Group("1", layout="floating"),
    2: Group("2", layout="tile"),
    3: Group("3", layout="monadwide"),
    4: Group("4", layout="monadwide"),
    5: Group("5"),
    6: Group("6"),
    7: Group("7"),
    8: Group("8"),
    9: Group("9"),
    0: Group("0", layout="max"),
}

# groups = [Group(i) for i in "1234567890"]
groups = [escritorios[i] for i in escritorios]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

# Formas de colocar los paneles
# funcion colores bordes

conf_layout = {
    'border_focus': "#0000ff",
    'border_width': 2,
    'margin': 2
}

layouts = [
    layout.MonadTall(**conf_layout),
    layout.Floating(**conf_layout),
    layout.Max(),
    layout.MonadWide(**conf_layout),
    layout.Tile(**conf_layout),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Zoomy(),
    # layout.TreeTab(),
    # layout.Matrix(),
    # layout.Bsp(),
    # layout.VerticalTile(),
    # layout.RatioTile(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=1,
)
extension_defaults = widget_defaults.copy()

# Pantalla
screens = [
    Screen(
        # Barra
        top=bar.Bar(
            [
                # Para el wifi, memoria y cpu se debe instalr una dependencia de pip 'psutil'

                widget.CurrentLayout(),
                widget.GroupBox(
                    active="#ff0000",
                    highlight_method='block',
                ),
                widget.Sep(background="#ff0000"),
                widget.Spacer(),
                widget.WindowName(
                    max_chars=40,
                ),
                widget.Spacer(),
                widget.Sep(background="#ff0000"),
                widget.Net(),
                widget.Sep(background="#ff0000"),
                widget.Memory(),
                widget.Sep(background="#ff0000"),
                widget.CPU(),
                widget.Sep(background="#ff0000"),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.PulseVolume(
                    background="#333cff",
                    foreground="#000000",
                ),
                widget.Battery(
                    background="#ffff33",
                    charge_char="#",
                    foreground="#000000",
                    format='{char} {percent:2.0%} {hour:d}:{min:02d}',
                    full_char="$",
                    low_background="#ff0000",
                    low_foreground=0.1,
                ),
                widget.QuickExit(),
            ],
            16,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
