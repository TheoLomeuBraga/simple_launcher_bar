 
from config import *

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GdkPixbuf, Gdk

import os


def resize_icon(icon_name, width, height):
    themed_icon = Gio.ThemedIcon.new(icon_name)
    icon_info = Gtk.IconTheme.get_default().lookup_by_gicon(themed_icon, 48, Gtk.IconLookupFlags.GENERIC_FALLBACK)

    if icon_info:
        pixbuf = icon_info.load_icon()
        scaled_pixbuf = pixbuf.scale_simple(width, height, GdkPixbuf.InterpType.BILINEAR)
        return scaled_pixbuf

    return None

def launcher_button(widget, argument):
    os.system(argument + " &")

def getResolution():
    ret = [0,0]
    screen = Gdk.Screen.get_default()
    monitor = screen.get_monitor_at_window(screen.get_active_window())
    geometry = screen.get_monitor_geometry(monitor)
    ret[0] = geometry.width
    ret[1] = geometry.height
    return ret
    

class MyWindow(Gtk.Window):

    

    def __init__(self):
        Gtk.Window.__init__(self, title="launchers")

        resolution = getResolution()

        if side == Sides.LEFT:
            self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.move(0, (resolution[1] / 2) - ((size * len(launchers)) / 2))
        if side == Sides.RIGHT:
            self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            self.move(resolution[0] - size ,(resolution[1] / 2) - ((size * len(launchers)) / 2))
        if side == Sides.TOP:
            self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            self.move((resolution[0] / 2) - ((size * len(launchers)) / 2), 0)
        if side == Sides.DOWN:
            self.box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            self.move((resolution[0] / 2) - ((size * len(launchers)) / 2),resolution[1] - size )

        self.add(self.box)

        for l in launchers:
            image = Gtk.Image.new_from_gicon(resize_icon(l.icon,size,size), Gtk.IconSize.BUTTON)

            button = Gtk.Button()
            button.set_image(image)
            button.set_size_request(size, size)
            button.set_tooltip_text(l.name)
            button.connect("clicked", launcher_button, l.command)
            self.box.pack_start(button, True, True, 0)

        

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
