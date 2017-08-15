print("Loading - this may take a couple of seconds.")
# Although having print function before imports in a script is considered
# really bad, I think it is really needed here, as it can take up to 
# 10(+) seconds to import everything (apt package is the biggest consumer here).
# If there were no print at the beggining, one could think that script is broken,
# because it doesn't output anything for so long.
import subprocess
import os 
import random
import apt
import configparser

def install_package_with_apt(package_name):
	"""
        Checks if user has a package with <package_name> installed.
        Tries to install it if:
            1. users hasn't got it installed   AND
	    2. agrees to install it.
        """
	cache = apt.Cache()
	if not cache[package_name].is_installed:
		pkg = cache[package_name]
		i = input("Package '{}' is not installed. Do you want to install it now?\n(Y/n):".format(package_name))
		if i == "Y":
			print("OK, please wait..")
			pkg.mark_install()
			cache.commit()
		else:
			print("Declined to install '{}'.".format(package_name))
	else:
		print("Package '{}' is already installed on this pi.".format(package_name))



if __name__ == "__main__":

    # Install the mpg123 if not already installed.
    install_package_by_apt("mpg123")


    # Read the config.ini file
    parser = configparser.SafeConfigParser()
    parser.read("config.ini")
    MUSIC_DIR = parser.get("main","MUSIC_DIR")
    BROADCAST_FREQUENCY = parser.get("main","BROADCAST_FREQUENCY") # In megahertz (MHz)
    RANDOM = parser.get("main","RANDOM")



    # Pipe stuff
    music_pipe_r,music_pipe_w = os.pipe()
    dev_null = open(os.devnull, "w")


    # Start the pifm process
    PiFMprocess = subprocess.Popen(["./pifm","-",BROADCAST_FREQUENCY,"48000", "stereo"], stdin=music_pipe_r, stdout=dev_null)

    print("Welcome to PiRadio!")
    print("PiFM process started. {} MHz, 48KHz bitrate, stereo.".format(BROADCAST_FREQUENCY))
    print("Random (shuffling) is set to {}".format(RANDOM))

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
                print("Emitting song <{}>.".format(file))
                subprocess.call(["sudo","/usr/bin/mpg123","-s","-r 48000",file],stdout=music_pipe_w, stderr=dev_null)

# TODO (stjepanbrkic): refactor code - use logging module instead of print.
