# Project imports
from sock import SocketControl
from chatwindow import ChatWindow

class Chat:
	def __init__(self):
		# Main Window
		self.window = ChatWindow(self)

		# Socket Controll
		self.sock_control = SocketControl()
		
	def show(self):
		self.window.show()
