import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyPersonalStatsWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="My Personal Stats")
        
        # Set the default size of the window
        self.set_default_size(700, 700)
        
        # Create a label and add it to the window
        label = Gtk.Label(label="Welcome to My Personal Stats!")
        self.add(label)
        
        # Optional: Set border width
        self.set_border_width(10)
        
    def on_destroy(self, widget):
        Gtk.main_quit()

# Create an instance of the window
win = MyPersonalStatsWindow()
# Connect the destroy event to the on_destroy method
win.connect("destroy", win.on_destroy)
# Show all widgets in the window
win.show_all()
# Start the GTK main loop
Gtk.main()
