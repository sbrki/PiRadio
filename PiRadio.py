#sudo ./pifm left_right.wav 103.3 22050 mono

import subprocess
import os 
import random

MUSIC_DIR="music"
BROADCAST_FREQUENCY="97.8" #MHz
FREQUENCY="48000" #KHz  , related to mp3 "quality"
CHANNELS="stereo"
RANDOM=True


while True:
	file_list = []
	for root, folders, files in os.walk(MUSIC_DIR):
		folders.sort()
		files.sort()
		for filename in files:
			if ".wav" in filename or ".WAV" in filename:
				file_list.append(os.path.join(root, filename))

 

	if RANDOM:
		random.shuffle(file_list)
	for file in file_list:
		print("***********")
		print("Now rocking file <{}> at {} MHz.".format(file, BROADCAST_FREQUENCY))
		print("***********")
		subprocess.call(["sudo","./pifm", file, BROADCAST_FREQUENCY, FREQUENCY, CHANNELS ])
