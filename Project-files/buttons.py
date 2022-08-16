import parameters as pr
import pygame

class Label:

	def __init__(self, button_text, button_type, x_pos, y_pos, width, height):

		self.button_text = button_text
		self.button_type = button_type
		self.height = height
		self.width = width
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.colour =  (220,220,220)
		self.rectangle = pygame.Rect(self.x_pos, self.y_pos,  self.width, self.height)
		self.draw_button()

		


	def __str__(self):
		return self.button_text

	def draw_button(self):
		text_width, text_height = pr.game_font.get_rect(f'{self.button_text}')[2:4]
		text_field=(int(self.x_pos + (self.width-text_width)/2), int(self.y_pos + (self.height - text_height)/2)) # Position of the text for centering
		pygame.draw.rect(pr.window, (0, 0, 0), (self.x_pos-2, self.y_pos-2, self.width+4,self.height+4)) # Draws the black border
		pygame.draw.rect(pr.window, self.colour, self.rectangle ) # Draws grey rectangle
		text = pr.game_font.render_to(pr.window, text_field, self.button_text, (0, 0, 0)) # writes text
		pygame.display.update((self.x_pos-2, self.y_pos-2,  self.width+4,self.height+4)) # Updates the screen for the button

	def get_type(self):
		return self.button_type

	def change_name(self, text):
		self.button_text = str(text)
		self.draw_button()

	def get_position(self):
		return self.rectangle


class Button(Label):

	def __init__(self, button_text, button_type, x_pos, y_pos, width, height):
		super().__init__(button_text, button_type, x_pos, y_pos, width, height)
		self.clicked = False
		pr.button_list.append(self)
		if self.button_type not in pr.state_toggle.keys():
			pr.state_toggle[button_type] = []
		pr.state_toggle[button_type].append(self)
		self.draw_button()

	def clicked_button(self):
		self.colour = (150,150,150)
		self.draw_button()
		self.clicked = True
		

	def unclick_button(self):
		self.colour = (220,220,220)
		self.draw_button()
		self.clicked = False

	def is_clicked(self):
		return self.clicked

class Toggle(Button):

	def toggle_state(self):
		for toggle in pr.state_toggle[self.get_type()]:
			toggle.unclick_button()
		self.clicked_button() 

class Switch(Button):

	def toggle_state(self):

		if self.is_clicked():
			self.unclick_button()
		else:
			self.clicked_button()

class Title:

	def __init__(self, button_text, button_type, x_pos, y_pos, width, height):

		self.button_text = button_text
		self.button_type = button_type
		self.height = height
		self.width = width
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.colour =  (255,255,255)
		self.rectangle = pygame.Rect(self.x_pos, self.y_pos,  self.width, self.height)
		self.draw_title()

	def get_position(self):
		return self.rectangle

	def draw_title(self):
		text_width, text_height = pr.game_font.get_rect(f'{self.button_text}')[2:4]
		text_field=(int(self.x_pos + (self.width-text_width)/2), int(self.y_pos + (self.height - text_height)/2)) # Position of the text for centering
		pygame.draw.line(pr.window, (0, 0, 0), (self.x_pos, self.y_pos+self.height), (self.x_pos+self.width,self.y_pos+self.height)) # Draws the black border
		#pygame.draw.rect(pr.window, self.colour, self.rectangle ) # Draws grey rectangle
		text = pr.game_font.render_to(pr.window, text_field, self.button_text, (0, 0, 0)) # writes text
		pygame.display.update((self.x_pos-2, self.y_pos-2,  self.width+4,self.height+4)) # Updates the screen for the button

def button_group_placement(button_number, title_button):

	# button number placement
	# 1    2
	# 3    4 etc

	title_location = list(title_button.get_position())

	if not button_number % 2:
		left = 1270
		top = int(title_location[1] + 60 * button_number/2)

	elif not button_number % 1:
		left = 1030
		top = int(title_location[1] + 60 * ((button_number-1)/2 + 1))

	width, height = 200, 30

	return left, top, width, height
	
	

	

