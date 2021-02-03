from PIL import Image 
import numpy as np

def sepia(image_path, k):
	
	image = Image.open(image_path)
	img = np.array(image)

	RGB = np.matrix([[ 0.393 + 0.607 * (1 - k), 0.769 - 0.769 * (1 - k), 0.189 - 0.189 * (1 - k)],
					[ 0.349 - 0.349 * (1 - k), 0.686 + 0.314 * (1 - k), 0.168 - 0.168 * (1 - k)],
					[ 0.272 - 0.349 * (1 - k), 0.534 - 0.534* (1 - k), 0.131 + 0.869 * (1 - k)]])

	filt = np.array([x * RGB.T for x in img] )

	filt[np.where(filt>255)] = 255

	return Image.fromarray(filt.astype('uint8'))


n = sepia('butiful.jpg', 0.5)
n.show()

