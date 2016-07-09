print("Loading.. this may take a few seconds.")
import subprocess
import os 
import random
import apt


#check if user has mpg123 installed
cache = apt.Cache()
if not cache["mpg123"].is_installed:
	pkg = cache["mpg123"]
	i=input("Module 'mpg123' is not installed. Do you want to install it now?\n(YES/NO):")
	if i=="YES":
		print("OK, please wait..")
		pkg.mark_install()
		cache.commit()
	else:
		print("Declined to install 'mpg123'.")
else:
	print("Module 'mpg123' is already installed on this pi.")



#config
MUSIC_DIR="music"
BROADCAST_FREQUENCY="97.8" #MHz
RANDOM=True



#pipe stuff
music_pipe_r,music_pipe_w= os.pipe()
dev_null=open(os.devnull, "w")


#start the pifm process
PiFMprocess = subprocess.Popen(["./pifm","-",BROADCAST_FREQUENCY,"48000", "stereo"], stdin=music_pipe_r, stdout=dev_null)
print("PiFM process started. {} MHz, 48KHz bitrate, stereo.".format(BROADCAST_FREQUENCY))


while True:
	file_list = []
	for root, folders, files in os.walk(MUSIC_DIR):
		folders.sort()
		files.sort()
		for filename in files:
			if "NOT" not in root and "NOT" not in filename:
				file_list.append(os.path.join(root, filename))

 

	if RANDOM:
		random.shuffle(file_list)


	for file in file_list:
		print("***********")
		print("Now rocking file <{}> at {} MHz.".format(file, BROADCAST_FREQUENCY))
		print("***********")
		subprocess.call(["sudo","/usr/bin/mpg123","-s","-r 48000",file],stdout=music_pipe_w, stderr=dev_null)
