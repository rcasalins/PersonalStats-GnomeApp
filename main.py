import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

class MyPersonalStatsWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Personal Stats")
        self.set_default_size(700, 700)

        # Create a header bar
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "My Personal Stats"
        self.set_titlebar(header_bar)

        # Create the "+" button in the header bar
        add_button = Gtk.Button()
        add_button.set_image(Gtk.Image.new_from_icon_name("list-add-symbolic", Gtk.IconSize.BUTTON))
        add_button.connect("clicked", self.on_add_button_clicked)
        header_bar.pack_start(add_button)

        # Create a box to hold widgets
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

    def on_add_button_clicked(self, widget):
        # Create a square button in the middle of the window
        square_button = Gtk.Button(label="Square")
        self.box.pack_start(square_button, True, True, 0)
        square_button.connect("clicked", self.on_square_button_clicked)

        # Show all widgets
        self.show_all()

    def on_square_button_clicked(self, widget):
        print("Square button clicked!")

win = MyPersonalStatsWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
