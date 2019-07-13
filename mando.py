################################
## Animación del mando de NES ##
################################

import cv2

# Dibuja el arrglo de movimientos sobre el mando
def draw_buttons(moves):
	img = cv2.imread('mando.jpg')
	overlay = img.copy()
	for move in moves:
		if move=="left":
			cv2.circle(img,(53,112), 15, (50,255,0), -1)
		if move=="right":
			cv2.circle(img,(105,112), 15, (50,255,0), -1)
		if move=="up":
			cv2.circle(img,(78,86), 15, (50,255,0), -1)
		if move=="down":
			cv2.circle(img,(78,138), 15, (50,255,0), -1)
		if move=="a":
			cv2.circle(img,(376,138), 30, (50,255,0), -1)
		if move=="b":
			cv2.circle(img,(316,138), 30, (50,255,0), -1)
	# Factor de tranparencia
	alpha = 0.5
	image_new = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
	return image_new

# Obtiene el arreglo de moviemientos del arreglo de acciones
def get_moves(action):
	moves = []
	if action[6]:
		moves.append("left")
	if action[7]:
		moves.append("right")
	if action[4]:
		moves.append("up")
	if action[5]:
		moves.append("down")
	if action[8]:
		moves.append("a")
	if action[0]:
		moves.append("b")
	return moves
