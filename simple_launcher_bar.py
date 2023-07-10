 
from config import *

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GdkPixbuf

import os


def resize_icon(icon_name, width, height):
    # Create a themed icon
    themed_icon = Gio.ThemedIcon.new(icon_name)

    # Load the icon
    icon_info = Gtk.IconTheme.get_default().lookup_by_gicon(themed_icon, 48, Gtk.IconLookupFlags.GENERIC_FALLBACK)

    if icon_info:
        # Get the pixbuf
        pixbuf = icon_info.load_icon()

        # Scale the pixbuf
        scaled_pixbuf = pixbuf.scale_simple(width, height, GdkPixbuf.InterpType.BILINEAR)

        return scaled_pixbuf

    return None

def launcher_button(widget, argument):
    os.system(argument + " &")

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="launchers")

        # Create a vertical box to hold the buttons
        if side == Sides.LEFT or side == Sides.RIGHT:
            self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        elif side == Sides.TOP or side == Sides.DOWN:
            self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        self.add(self.box)

        for l in launchers:
            image = Gtk.Image.new_from_gicon(resize_icon(l.icon,size,size), Gtk.IconSize.BUTTON)

            button = Gtk.Button()
            button.set_image(image)
            button.set_size_request(size, size)
            button.set_tooltip_text(l.name)
            button.connect("clicked", lambda widget: launcher_button(widget, l.command))

            self.box.pack_start(button, True, True, 0)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
