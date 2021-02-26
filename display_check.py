import pyglet
def display_check():
	display = pyglet.canvas.get_display()
	screens = display.get_screens()
	cont1=len(screens)
	if cont1!=1:
		exit()