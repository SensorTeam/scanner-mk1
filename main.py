import shutil
import requests

# Constants
# -----------------------------------------------

URL = 'http://flashair'
PATH = '/DCIM/100__TSB'

# Functions
# -----------------------------------------------

def list_images(url, path):
	r = requests.get(
			'{}/command.cgi'.format(url), 
			params={
				'op': 100,
				'DIR': path
			}
		)
	lines = r.text.split('\n')
	images = []
	for line in lines[1:]:
		values = line.split(',')
		if len(values) > 2:
			image = values[1].strip()
			images.append(image)
	return images

def download_image(url, to):
	r = requests.get(url, stream=True)
	if r.status_code == 200:
		with open(to, 'wb') as f:
			for chunk in r:
				f.write(chunk)

def main():
	images = list_images(URL, PATH)
	latest_image = images[len(images)-1]
	image_url = URL + PATH + '/' + latest_image
	to = 'output/' + latest_image

	print(image_url)

	download_image(image_url, to)

# Main
# -----------------------------------------------

if __name__ == '__main__':
	main()