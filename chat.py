import pygtk
pygtk.require('2.0')
import gtk

# Project imports
from sock import SocketControl

class Chat:
	def __init__(self):
		# Let's build the interface
		self.build_interface()

		# Our socket controller
		sock = SocketControl()

	def build_interface(self):
		# Creating the Window
		self.window = gtk.Window()
		self.window.set_title("GTK Chat")
		self.window.resize(640, 480)

		# Events
		self.window.connect("delete_event", self.delete_event)
		self.window.connect("destroy", self.destroy)


	def show(self):
		self.window.show()
		self.window.show_all()

		gtk.main()

	
	# EVENTS METHODS
	def destroy(self, widget, data=None):
		gtk.main_quit()
	
	def delete_event(self, widget, event, data=None):
		print "Deleting..."
		
		return False
