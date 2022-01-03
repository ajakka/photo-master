from matplotlib import pyplot, image
from numpy.lib.function_base import copy

# From Scratch Image Processing

class FSImageProcessing:
	org_image: None
	src_images = []

	def __init__(self, org_image):
		self.org_image = image.imread(org_image)

	def gray(self, brightness=1):
		temp_image = self.copy_image()
		if brightness >= 0:
			for row in temp_image:
				for pixel in row:
					med = (pixel[0]+pixel[1]+pixel[2]/3) * brightness
					pixel[0] = min(med, 1)
					pixel[1] = min(med, 1)
					pixel[2] = min(med, 1)
			self.save_image(temp_image)

	def brighten(self, brightness=1):
		temp_image = self.copy_image()
		if brightness >= 0:
			for row in temp_image:
				for pixel in row:
					pixel[0] = min(pixel[0] * brightness, 1)
					pixel[1] = min(pixel[1] * brightness, 1)
					pixel[2] = min(pixel[2] * brightness, 1)
			self.save_image(temp_image)

	def copy_image(self): 
		return copy(self.org_image)

	def save_image(self, saved_image): 
		self.src_images.append(saved_image)

	def show_image(self):
		cols, rows = 5, max((len(self.src_images)) // 5, 1) + 1
		fig = pyplot.figure(figsize=(10, 5))

		for i in range(1, len(self.src_images)+1):
			fig.add_subplot(rows, cols, i)
			pyplot.imshow(self.src_images[i-1])
			pyplot.axis('off')
		
		fig.add_subplot(rows, cols, len(self.src_images)+1)
		pyplot.imshow(self.org_image)
		pyplot.axis('off')
		pyplot.text(0, 450, 'Original')

		pyplot.show()