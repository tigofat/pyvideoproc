from tkinter import Tk, Button

class Window:

	def __init__(self):

		WIDTH, HEIGHT = 200, 80

		self.master = Tk()
		self.master.geometry(f'{WIDTH}x{HEIGHT}')
		self.master.title('Window')
		self.button = Button(self.master, text='Stop', command=self.stop)
		self.button.pack()

		self.running = False

	def show(self):
		self.master.update()

	def stop(self):
		self.running = False