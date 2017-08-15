# PiRadio
PiRadio is a small and lightweight Python3 radio script that is based on PiFM project

## Requirements:
**configparser**, used for parsing the configuration file.

You can get it by running `sudo pip3 install configparser`.
<br>

Also, **mpeg123** must be installed on the Pi order for the script to run.

*Note: If you don't have mpeg123 installed, script can install it for you. Just run PiRadio.py and hit yes when asked if you wish to install mpeg123.*

## Usage:

**1. Creating a music directory**

Create a `music` folder inside of PiRadio folder and place your music there.

Songs can be in whichever format you prefer, if *mpg123* supports it.
&nbsp;

*Note:* mpg123 supports a whole lot of music formats, including **mp3**.

*Note: you don't have to name your folder 'music', as you can edit the config file and change the 'MUSIC_DIR' value.*

---
**2. Editing your settings**

Edit the settings in `config.ini` file to suit your interest.

The `BROADCAST_FREQUENCY` is measured in *MHz* (Megaherz) and it sets the radio emmiter frequency.

The `RANDOM` tells PiRadio to shuffle the songs (play them in a random order).

---
**3. Make your antenna**

Connect any kind of wire (20 cm will do) to **GPIO Pin 4** on your Raspberry Pi.

![props to mcuoneclipse.com](http://i.imgur.com/zeowQRH.png)

---
**4. Run PiRadio.py**

Run `sudo python3 PiRadio.py` and enjoy your radio!

---
### DISCLAIMER: Where I live, It is legal to broadcast on unassigned FM frequencies if the source is less powerful than 0.3 W.
### Before broadcasting, you must check your (local, or state) laws.
### I am NOT responsible for any trouble you do if you violate your laws.
