# Project imports
from sock import SocketControl
from chatwindow import ChatWindow

class Chat:
	def __init__(self):
		self.window = ChatWindow(self)
		
	def show(self):
		self.window.show()
