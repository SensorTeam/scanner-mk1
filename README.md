# Scanner

Streams and downloads the latest image from a Toshiba FlashAir SD card.

## Requirements

* `python3`
* `pip`
* `virtualenv`

## Setup

1. Clone this repo
2. Setup `virtualenv -p python3 venv`
3. Activate `. ./venv/bin/activate` (or `. ./venv/Scripts/activate` for Windows Powershell)
4. Install package dependencies with `pip install -r requirements.txt`

## Usage

The following functions can be used by The System:

* `is_connected()` — which checks if the SD card server is still alive
* `get_image_list()` — which returns a list of all the files currently on the SD card
* `download_latest_image()` — which downloads the latest image (as two files: `.CR2` and `.JPG`)