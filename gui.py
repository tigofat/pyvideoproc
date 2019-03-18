from tkinter import Tk

class Window:

	def __init__(self):

		WIDTH, HEIGHT = 200, 80

		self.master = Tk()
		self.master.geometry(f'{WIDTH}x{HEIGHT}')
		self.master.title('Window')

		self.running = False

	def show(self):
		self.master.update()