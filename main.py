import shutil
import requests

# Constants
# -----------------------------------------------

URL = 'http://flashair'
PATH = '/DCIM/100__TSB'

# Functions
# -----------------------------------------------

def get_image_list(url, path):
	# Returns a list of all the files currently on the SD card
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
	# Downloads an image from the SD card to the specified output path
	r = requests.get(url, stream=True)
	if r.status_code == 200:
		with open(to, 'wb') as f:
			for chunk in r:
				f.write(chunk)

def is_alive(url):
	# Check if the SD card server is still alive
	r = requests.get(url)
	if r.status_code == 200:
		return True
	else:
		return False

def main():
	images = []
	prev_len = len(images)

	if is_alive(URL):
		print('CONNECTED')
	else:
		print('COULD NOT CONNECT')

	while is_alive(URL):
		images = get_image_list(URL, PATH)
		new_len = len(images)

		if new_len > prev_len:
			prev_len = new_len

			latest_image = images[-1]
			latest_image_url = URL + PATH + '/' + latest_image

			output_path = 'output/' + latest_image
			download_image(latest_image_url, output_path)

			print('DOWNLOADED: ', latest_image)
	print('DISCONNECTED')


# Main
# -----------------------------------------------

if __name__ == '__main__':
	main()