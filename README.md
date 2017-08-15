# PiRadio
PiRadio is a small and lightweight Python3 radio script that is based on the PiFM project


## But why?

PiRadio came to life when I was tinkering with MakeMagazine-s RBPi Pirate Radio project. While cool, the project required you to download and burn the image they provided (couple of GBs), which was inconvenient. 

Also, my Pi was randomly freezing up and experiencing hiccups while running the burned image. I still don't know why.

Anyway, I decided to build my own version of the project.

## Requirements:
**Python3 libraries:**

* **configparser**, used for parsing the configuration file.You can get it by running `sudo pip3 install configparser`.

**Other libraries:**

* **mpg123**, for transcoding the music files. You can get it by running `sudo apt-get install mpg123`

*Note*: If you don't have mpg123 installed, PiRadio can install it for you. Just run PiRadio.py and hit yes when asked if you wish to install mpg123.

## Usage:

**0. Download the project**

You can download the project via github as a ZIP, or do a `git pull https://github.com/whiteShtef/PiRadio`.

---

**1. Populate the music directory**

Inside of the project directory lies the `music` directory. Place your music files inside. It already **comes preloaded with one song** if you just want to test your PiRadio.

Songs can be in whichever format you prefer, if *mpg123* supports it (mpg123 supports a whole lot of music formats, including **mp3**.).
&nbsp;

*Note:* you can edit the config file and change the `MUSIC_DIR` value.

---
**2. Editing your settings**

Edit the settings in `config.ini` file to suit your interest.

The `BROADCAST_FREQUENCY` is measured in *MHz* (Megaherz) and it sets the radio emmiter frequency.

The `RANDOM` tells PiRadio to shuffle the songs (play them in a random order).

---
**3. Make your antenna**

Connect any kind of wire to **GPIO Pin 4** on your Raspberry Pi.

If you don't connect any wire, the broadcasting range will be just a cople of inches.

The wire doesn't need to be long, **10 cm/4 inches of wire is enough.**

![props to mcuoneclipse.com](http://i.imgur.com/zeowQRH.png)

*Image taken from mcuoneclipse.com*

---
**4. Run PiRadio.py**

Run `sudo python3 PiRadio.py` and enjoy your radio!

---
### DISCLAIMER

Where I live, It is legal to broadcast on unassigned FM frequencies if the source is less powerful than 0.3 W.

**Before broadcasting, you must check your (local, or state) laws. I am NOT responsible for any trouble you do if you violate your laws.**
